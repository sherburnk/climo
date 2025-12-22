import streamlit as st
import numpy as np
import matplotlib.colors as mcolors
import json
import urllib.request
from datetime import datetime, timedelta
import climoplots_config as cf
import pandas as pd
import pytz

# --- TIMEZONE UTILITY ---

def get_local_now(state_code):
    """Returns current datetime localized to the selected state."""
    tz_map = {
        "HI": "Pacific/Honolulu", "AK": "America/Anchorage",
        "CA": "America/Los_Angeles", "OR": "America/Los_Angeles", "WA": "America/Los_Angeles", "NV": "America/Los_Angeles",
        "AZ": "America/Phoenix", "MT": "America/Denver", "ID": "America/Denver", "WY": "America/Denver", "CO": "America/Denver", "UT": "America/Denver", "NM": "America/Denver",
        "TX": "America/Chicago", "OK": "America/Chicago", "KS": "America/Chicago", "NE": "America/Chicago", "SD": "America/Chicago", "ND": "America/Chicago", "MN": "America/Chicago", "IA": "America/Chicago", "MO": "America/Chicago", "AR": "America/Chicago", "LA": "America/Chicago", "WI": "America/Chicago", "IL": "America/Chicago", "MS": "America/Chicago", "AL": "America/Chicago",
        "FL": "America/New_York", "GA": "America/New_York", "SC": "America/New_York", "NC": "America/New_York", "VA": "America/New_York", "WV": "America/New_York", "KY": "America/New_York", "TN": "America/New_York", "OH": "America/New_York", "MI": "America/New_York", "IN": "America/New_York", "PA": "America/New_York", "NY": "America/New_York", "NJ": "America/New_York", "CT": "America/New_York", "RI": "America/New_York", "MA": "America/New_York", "VT": "America/New_York", "NH": "America/New_York", "ME": "America/New_York", "MD": "America/New_York", "DE": "America/New_York", "DC": "America/New_York"
    }
    tz_name = tz_map.get(state_code, "UTC")
    return datetime.now(pytz.timezone(tz_name))

# List of US States
US_STATES = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
             "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", 
             "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", 
             "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", 
             "UT", "VA", "VT", "WA", "WI", "WV", "WY"]

# --- CORE UTILITIES ---

@st.cache_data(ttl=3600)
def query_acis(params, endpoint="StnData"):
    inputdata = json.dumps(params).encode("utf-8")
    headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
    url = f"https://data.rcc-acis.org/{endpoint}"
    req = urllib.request.Request(url, data=inputdata, headers=headers, method="POST")
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read())

def get_stations_by_state(state_code):
    params = {"state": state_code, "meta": "name,sids,ll,state,valid_daterange", "elems": "maxt"}
    data = query_acis(params, endpoint="StnMeta")
    threadex, icao = [], []
    if 'meta' in data:
        for m in data['meta']:
            sids = m.get('sids', [])
            thr_sid = next((s.split()[0] for s in sids if s.endswith(' 9') or 'thr' in s.lower()), None)
            icao_sid = next((s.split()[0] for s in sids if s.endswith(' 5') or (len(s.split()[0]) == 4 and s.split()[0].isalpha())), None)
            if not thr_sid and not icao_sid: continue
            lat, lon = (m['ll'][1], m['ll'][0]) if 'll' in m else (0.0, 0.0)
            if lat is None: continue
            por_str = "Unknown"
            vdr = m.get('valid_daterange', [])
            try:
                if vdr and isinstance(vdr, list) and len(vdr) > 0:
                    dates = vdr[0][0]
                    if len(dates) >= 2: por_str = f"{dates.split('-')[0]}"
            except: por_str = "Unknown"
            entry = {"name": m['name'], "lat": lat, "lon": lon, "por_display": por_str, "sid": thr_sid if thr_sid else icao_sid, "type": "ThreadEx" if thr_sid else "ICAO"}
            if thr_sid: threadex.append(entry)
            else: icao.append(entry)
    full_list = sorted(threadex, key=lambda x: x['name']) + sorted(icao, key=lambda x: x['name'])
    if not full_list: return pd.DataFrame()
    df = pd.DataFrame(full_list)
    df['display_name'] = df.apply(lambda x: f"{x['name']} ({x['sid']})", axis=1)
    return df

# --- DATA FETCHING ---

def get_sidebar_summary(sid, mode, target_date):
    date_str = target_date.strftime("%Y%m%d")
    if mode == "Daily Records": 
        config, elems = cf.elems_rec, ["maxt", "mint", "pcpn", "snow", "avgt"]
    elif mode == "Normals": 
        config, elems = cf.elems_avg, [{"name": e['aname'], "normal": "1"} for e in cf.elems_avg.values()]
    elif mode == "YTD Observations": 
        config, elems = cf.elems_ytd, [{"name": e['aname']} for e in cf.elems_ytd.values()]
    else: 
        config, elems = cf.elems_dep, [{"name": e['aname'], "normal": "departure"} for e in cf.elems_dep.values()]

    data = query_acis({"sid": sid, "sdate": date_str, "edate": date_str, "elems": elems})
    summary = []
    if 'data' in data and data['data']:
        row = data['data'][0]
        por_params = {"sid": sid, "sdate": "por", "edate": "por", "elems": ["maxt", "mint", "pcpn", "snow", "avgt"]}
        por_data = query_acis(por_params) if mode == "Daily Records" else None
        for i, (key, info) in enumerate(config.items()):
            if mode == "Daily Records" and por_data:
                val_idx = info['val']
                is_high = key in ['maxtmp', 'hmntmp', 'maxpcp', 'maxsnw', 'maxavg']
                day_records = [r for r in por_data['data'] if r[0][5:] == target_date.strftime("%m-%d")]
                vals = [(float(r[val_idx]) if r[val_idx] != "T" else 0.001, r[0][:4]) for r in day_records if r[val_idx] not in ["M", "S", "A"] and "A" not in str(r[val_idx])]
                if vals:
                    v, yr = max(vals) if is_high else min(vals)
                    summary.append({"label": info['title'], "val": v, "year": yr, "unit": info['unit']})
            else:
                try:
                    val = row[i+1]
                    if val not in ["M", "S", "A"]:
                        summary.append({"label": info['title'], "val": float(val) if val != "T" else 0.001, "year": None, "unit": info.get('unit', 'degrees')})
                except: continue
    return summary

def get_data_grids(sid, var_key, mode, local_now):
    cur_year = local_now.year
    if mode == "Daily Records":
        elem = cf.elems_rec[var_key]; params = {"sid": sid, "sdate": "por", "edate": "por", "elems": ["maxt", "mint", "pcpn", "snow", "avgt"]}
        idx, is_high = elem['val'], var_key in ['maxtmp', 'hmntmp', 'maxpcp', 'maxsnw', 'maxavg']
    elif mode == "Normals":
        elem = cf.elems_avg[var_key]; params = {"sid": sid, "sdate": f"{cur_year}0101", "edate": f"{cur_year}1231", "elems": [{"name": elem['aname'], "interval": "dly", "normal": "1"}]}
        idx, is_high = 1, True
    elif mode == "YTD Observations":
        elem = cf.elems_ytd[var_key]
        params = {"sid": sid, "sdate": f"{cur_year}0101", "edate": local_now.strftime("%Y%m%d"), "elems": [{"name": elem['aname'], "interval": "dly"}]}
        idx, is_high = 1, True
    else: # Departures
        elem = cf.elems_dep[var_key]
        params = {"sid": sid, "sdate": f"{cur_year}0101", "edate": local_now.strftime("%Y%m%d"), "elems": [{"name": elem['aname'], "interval": "dly", "normal": "departure"}]}
        idx, is_high = 1, True

    data = query_acis(params)
    v_grid, i_grid, n_grid = np.full((32, 12), -999.0 if is_high else 999.0), np.full((32, 12), "", dtype=object), np.zeros((32, 12), dtype=bool)
    if 'data' not in data: return None, None, None
    for r in data['data']:
        try:
            cyr, cmon, cday = int(r[0][:4]), int(r[0][5:7]), int(r[0][8:10])
            val = 0.001 if r[idx] == "T" else (float(r[idx]) if r[idx] not in ["M", "S", "A"] and "A" not in str(r[idx]) else None)
            if val is None: continue
            if mode == "Daily Records":
                if (is_high and val >= v_grid[cday-1][cmon-1]) or (not is_high and val <= v_grid[cday-1][cmon-1]):
                    v_grid[cday-1][cmon-1], i_grid[cday-1][cmon-1], n_grid[cday-1][cmon-1] = val, f"Year: {cyr}", (cyr == cur_year)
            else:
                v_grid[cday-1][cmon-1], i_grid[cday-1][cmon-1] = val, f"Date: {r[0]}" if mode != "Normals" else ""
        except: continue
    for m in range(12):
        valid = v_grid[:31, m][(v_grid[:31, m] != 999.0) & (v_grid[:31, m] != -999.0)]
        if len(valid) > 0: v_grid[31, m] = np.sum(valid) if any(x in var_key for x in ['pcp', 'snw']) else np.mean(valid)
    return v_grid, i_grid, n_grid

# --- STYLING & PAGE RENDERING ---

def get_style(val, var_key, mode, is_new, is_target):
    if val in [999.0, -999.0]: return "background-color: transparent; color: black;"
    if val == 0.001: return "background-color: #ffebcd; color: black;"
    if mode == "Departures": cmap, norm = (cf.brbgcmap, mcolors.Normalize(-1,1)) if 'pcp' in var_key else (cf.puorcmap, mcolors.Normalize(-6,6)) if 'snw' in var_key else (cf.rdburcmap, mcolors.Normalize(-25,25))
    else: cmap, norm = (cf.tcmap, mcolors.Normalize(-60,120)) if any(x in var_key for x in ['tmp', 'avg', 'maxt', 'mint', 'max', 'min']) else (cf.bugncmap, mcolors.Normalize(0,2)) if 'pcp' in var_key else (cf.pubucmap, mcolors.Normalize(0,12))
    rgba = cmap(norm(val)); style = f"background-color: {mcolors.to_hex(rgba)};"
    if is_new: style += " border: 3px solid black; font-weight: 900;"
    elif is_target: style += " outline: 3px solid yellow; z-index: 5; position: relative;"
    if not is_new: style += f" color: {'white' if (0.299*rgba[0] + 0.587*rgba[1] + 0.114*rgba[2]) < 0.45 else 'black'};"
    return style

def render_html_table(v_grid, i_grid, n_grid, var_key, mode, local_now):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    yest = local_now - timedelta(days=1)
    is_temp = any(x in var_key for x in ['tmp', 'avg', 'maxt', 'mint', 'max', 'min'])
    is_snow = 'snw' in var_key or 'snd' in var_key
    html = "<style>.climo-table { width: 100%; border-collapse: collapse; font-size: 18px; table-layout: fixed; color: black; } .climo-table th, .climo-table td { border: 1px solid #ccc; text-align: center; padding: 4px 0; font-weight: bold; } .climo-table th:not(.label-col) { width: 7.7%; } .climo-table thead th {background-color: #ddd !important;} .climo-table td:hover { outline: 3px solid #00ffff; z-index: 10; cursor: help; } .label-col { width: 60px; background-color: #ddd !important; } .summary-row { background-color: #eee; border-top: 2px solid black; }</style><table class='climo-table'><thead><tr><th class='label-col'>Day</th>" + "".join(f"<th>{m}</th>" for m in months) + "</tr></thead><tbody>"
    for d in range(32):
        html += f"<tr class='{'summary-row' if d == 31 else ''}'><td class='label-col'>{'Avg/Sum' if d == 31 else d+1}</td>"
        for m in range(12):
            val = v_grid[d][m]
            if val in [999.0, -999.0]: html += "<td>-</td>"; continue
            is_target = (d == yest.day-1 and m == yest.month-1) if mode in ["YTD Observations", "Departures"] else (d == local_now.day-1 and m == local_now.month-1)
            disp = "Trace" if val == 0.001 else (f"{int(round(val))}" if is_temp else f"{val:.1f}" if is_snow else f"{val:.2f}")
            html += f"<td title='{i_grid[d][m]}' style='{get_style(val, var_key, mode, n_grid[d][m], is_target)}'>{disp}</td>"
        html += "</tr>"
    return html + "</table>"

# --- UI ---

st.set_page_config(page_title="NWS Climate Hub", layout="wide", initial_sidebar_state="expanded")
st.markdown("""<style>[data-testid="stSidebar"] { min-width: 450px; max-width: 450px; } [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0.5rem; } [data-testid="stSidebar"] hr { margin-top: 10px; margin-bottom: 10px; }</style>""", unsafe_allow_html=True)

st.sidebar.header("Step 1: Select State")
state_sel = st.sidebar.selectbox("State", US_STATES, index=US_STATES.index("IL"))

with st.spinner("Finding ThreadEx & ICAO stations..."):
    df_stations = get_stations_by_state(state_sel)

if not df_stations.empty:
    st.sidebar.header("Step 2: Choose Location")
    site_disp = st.sidebar.selectbox("Select Station", df_stations['display_name'].tolist())
    selected_site = df_stations[df_stations['display_name'] == site_disp].iloc[0]
    sid = selected_site['sid']
else:
    st.sidebar.error("No valid ThreadEx or ICAO sites found."); st.stop()

mode = st.sidebar.radio("Category", ["Daily Records", "Normals", "YTD Observations", "Departures"])
st.sidebar.markdown("---")
st.sidebar.markdown("### Legend")
st.sidebar.markdown("🟨 **Yellow Outline**: Current / Target Day")
if mode == "Daily Records": st.sidebar.markdown("⬛ **Black Border**: Record set/tied this year")
st.sidebar.markdown("---")

elem_dict = {"Daily Records": cf.elems_rec, "Normals": cf.elems_avg, "YTD Observations": cf.elems_ytd, "Departures": cf.elems_dep}[mode]
friendly_map = {info['title']: key for key, info in elem_dict.items()}
selected_friendly = st.sidebar.selectbox("Climate Element", list(friendly_map.keys()))
var_key = friendly_map[selected_friendly]

with st.spinner("Processing..."):
    # GET LOCAL TIME FOR CALCULATIONS
    local_now = get_local_now(state_sel)
    yesterday = local_now - timedelta(days=1)
    
    target_dt = yesterday if mode in ["YTD Observations", "Departures"] else local_now
    summary = get_sidebar_summary(sid, mode, target_dt)
    
    st.sidebar.markdown(f"--- \n## {'Yesterday' if mode in ['YTD Observations', 'Departures'] else 'Today'} ({target_dt.strftime('%b %d')})")
    for itm in summary:
        if itm['val'] == 0.001: val_s, u = "Trace", ""
        else:
            u = '"' if "inches" in itm['unit'].lower() or "in" in itm['unit'].lower() else "°F"
            val_s = f"{itm['val']:.1f}" if "snow" in itm['label'].lower() else f"{itm['val']:.2f}" if "precip" in itm['label'].lower() else f"{int(round(itm['val']))}"
        st.sidebar.markdown(f"<div style='white-space: nowrap;'><b>{itm['label']}:</b> {val_s}{u}{' ('+itm['year']+')' if itm.get('year') else ''}</div>", unsafe_allow_html=True)

    v, i, n = get_data_grids(sid, var_key, mode, local_now)
    if v is not None:
        if mode in ["Daily Records"]:
            st.subheader(f"{selected_friendly} — {selected_site['name']} (records since {selected_site['por_display']})")
        else:
            st.subheader(f"{selected_friendly} — {selected_site['name']}")
        st.markdown(render_html_table(v, i, n, var_key, mode, local_now), unsafe_allow_html=True)
st.sidebar.markdown("")
st.sidebar.markdown("---")
st.sidebar.markdown("Data courtesy of the Applied Climate Information System (ACIS)")

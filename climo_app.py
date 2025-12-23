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
    tz_map = {
        "HI": "Pacific/Honolulu", "AK": "America/Anchorage",
        "CA": "America/Los_Angeles", "OR": "America/Los_Angeles", "WA": "America/Los_Angeles", "NV": "America/Los_Angeles",
        "AZ": "America/Phoenix", "MT": "America/Denver", "ID": "America/Denver", "WY": "America/Denver", "CO": "America/Denver", "UT": "America/Denver", "NM": "America/Denver",
        "TX": "America/Chicago", "OK": "America/Chicago", "KS": "America/Chicago", "NE": "America/Chicago", "SD": "America/Chicago", "ND": "America/Chicago", "MN": "America/Chicago", "IA": "America/Chicago", "MO": "America/Chicago", "AR": "America/Chicago", "LA": "America/Chicago", "WI": "America/Chicago", "IL": "America/Chicago", "MS": "America/Chicago", "AL": "America/Chicago",
        "FL": "America/New_York", "GA": "America/New_York", "SC": "America/New_York", "NC": "America/New_York", "VA": "America/New_York", "WV": "America/New_York", "KY": "America/New_York", "TN": "America/New_York", "OH": "America/New_York", "MI": "America/New_York", "IN": "America/New_York", "PA": "America/New_York", "NY": "America/New_York", "NJ": "America/New_York", "CT": "America/New_York", "RI": "America/New_York", "MA": "America/New_York", "VT": "America/New_York", "NH": "America/New_York", "ME": "America/New_York", "MD": "America/New_York", "DE": "America/New_York", "DC": "America/New_York"
    }
    tz_name = tz_map.get(state_code, "UTC")
    return datetime.now(pytz.timezone(tz_name))

US_STATES = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
             "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", 
             "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", 
             "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", 
             "UT", "VA", "VT", "WA", "WI", "WV", "WY"]

# --- DATA UTILITIES ---
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
            por_str = "Unknown"
            vdr = m.get('valid_daterange', [])
            try:
                if vdr and len(vdr) > 0: por_str = f"{vdr[0][0].split('-')[0]}"
            except: por_str = "Unknown"
            entry = {"name": m['name'], "por_display": por_str, "sid": thr_sid if thr_sid else icao_sid}
            if thr_sid: threadex.append(entry)
            else: icao.append(entry)
    df = pd.DataFrame(sorted(threadex, key=lambda x: x['name']) + sorted(icao, key=lambda x: x['name']))
    if not df.empty: df['display_name'] = df.apply(lambda x: f"{x['name']} ({x['sid']})", axis=1)
    return df

def get_sidebar_summary(sid, mode, target_date):
    date_str = target_date.strftime("%Y%m%d")
    summary = []
    if mode == "Daily Records":
        config = cf.elems_rec
        por_params = {"sid": sid, "sdate": "por", "edate": "por", "elems": ["maxt", "mint", "pcpn", "snow", "avgt"]}
        por_data = query_acis(por_params)
        if 'data' in por_data:
            target_mmdd = target_date.strftime("%m-%d")
            for key, info in config.items():
                val_idx, is_high = info['val'], key in ['maxtmp', 'hmntmp', 'maxpcp', 'maxsnw', 'maxavg']
                day_records = [r for r in por_data['data'] if r[0][5:] == target_mmdd]
                vals = []
                for r in day_records:
                    if r[val_idx] not in ["M", "S", "A"] and "A" not in str(r[val_idx]):
                        vals.append((0.001 if r[val_idx] == "T" else float(r[val_idx]), r[0][:4]))
                if vals:
                    v, yr = max(vals) if is_high else min(vals)
                    summary.append({"label": info['title'], "val": v, "year": yr})
        return summary
    else:
        config = cf.elems_avg if mode == "Normals" else (cf.elems_ytd if mode == "YTD Observations" else cf.elems_dep)
        elems = [{"name": e['aname'], "normal": ("1" if mode == "Normals" else "departure")} for e in config.values()]
        if mode == "YTD Observations":
            elems = [{"name": e['aname'], "duration": "ytd", "reduce": "sum"} if 'pcp' in e['aname'].lower() or 'snw' in e['aname'].lower() else {"name": e['aname']} for e in config.values()]
        data = query_acis({"sid": sid, "sdate": date_str, "edate": date_str, "elems": elems})
        if 'data' in data and data['data']:
            for i, (key, info) in enumerate(config.items()):
                val = data['data'][0][i+1]
                if val not in ["M", "S", "A"]:
                    summary.append({"label": info['title'], "val": float(val) if val != "T" else 0.001})
    return summary

def get_data_grids(sid, var_key, mode, local_now):
    cur_year = local_now.year
    if mode == "Daily Records":
        elem = cf.elems_rec[var_key]; params = {"sid": sid, "sdate": "por", "edate": "por", "elems": ["maxt", "mint", "pcpn", "snow", "avgt"]}
        idx, is_high = elem['val'], var_key in ['maxtmp', 'hmntmp', 'maxpcp', 'maxsnw', 'maxavg']
    else:
        elem = (cf.elems_avg[var_key] if mode == "Normals" else (cf.elems_ytd[var_key] if mode == "YTD Observations" else cf.elems_dep[var_key]))
        params = {"sid": sid, "sdate": f"{cur_year}0101", "edate": local_now.strftime("%Y%m%d"), "elems": [{"name": elem['aname'], "interval": "dly", "normal": ("1" if mode == "Normals" else ("departure" if mode == "Departures" else None))}]}
        idx, is_high = 1, True
    data = query_acis(params)
    v_grid, i_grid, n_grid = np.full((32, 12), -999.0 if is_high else 999.0), np.full((32, 12), "", dtype=object), np.zeros((32, 12), dtype=bool)
    if 'data' not in data: return None, None, None
    for r in data['data']:
        try:
            cyr, cmon, cday = int(r[0][:4]), int(r[0][5:7]), int(r[0][8:10])
            val = 0.001 if r[idx] == "T" else (float(r[idx]) if r[idx] not in ["M", "S", "A"] else None)
            if val is None: continue
            if mode == "Daily Records":
                if (is_high and val >= v_grid[cday-1][cmon-1]) or (not is_high and val <= v_grid[cday-1][cmon-1]):
                    v_grid[cday-1][cmon-1], i_grid[cday-1][cmon-1], n_grid[cday-1][cmon-1] = val, f"Year: {cyr}", (cyr == cur_year)
            else:
                v_grid[cday-1][cmon-1], i_grid[cday-1][cmon-1] = val, r[0]
        except: continue
    for m in range(12):
        valid = v_grid[:31, m][(v_grid[:31, m] != 999.0) & (v_grid[:31, m] != -999.0)]
        if len(valid) > 0: v_grid[31, m] = np.sum(valid) if any(x in var_key for x in ['pcp', 'snw']) else np.mean(valid)
    return v_grid, i_grid, n_grid

# --- STYLING ---
def get_style(val, var_key, mode, is_new, is_target):
    if val in [999.0, -999.0]: return "background-color: transparent;"
    if val == 0.001: return "background-color: #ffebcd; color: black;"
    vk = var_key.lower()
    if mode == "Departures":
        if 'pcp' in vk: cmap, norm = cf.brbgcmap, mcolors.Normalize(-1.5, 1.5)
        elif 'snw' in vk: cmap, norm = cf.puorcmap, mcolors.Normalize(-5, 5)
        else: cmap, norm = cf.rdburcmap, mcolors.Normalize(-20, 20)
    else:
        if 'pcp' in vk: cmap, norm = cf.qacmap, mcolors.Normalize(0, 2.0)
        elif 'snw' in vk: cmap, norm = cf.sacmap, mcolors.Normalize(0, 6.0)
        else: cmap, norm = cf.tcmap, mcolors.Normalize(-20, 110)
    rgba = cmap(norm(val))
    style = f"background-color: {mcolors.to_hex(rgba)};"
    if is_new: style += " border: 2px solid black; font-weight: 900;"
    elif is_target: style += " outline: 3px solid yellow; outline-offset: -3px; z-index: 5;"
    lum = (0.299*rgba[0] + 0.587*rgba[1] + 0.114*rgba[2])
    style += f" color: {'white' if lum < 0.4 else 'black'};"
    return style

def render_html_table(v_grid, i_grid, n_grid, var_key, mode, local_now):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    yest, vk = local_now - timedelta(days=1), var_key.lower()
    is_precip, is_snow = 'pcp' in vk, 'snw' in vk
    row_count = 31 if mode == "Daily Records" else 32

    html = """
    <style>
        .scroll-container { width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; margin-top: 10px; position: relative; }
        .climo-table { min-width: 900px; width: 100%; border-collapse: collapse; font-size: 18px; table-layout: fixed; }
        .climo-table th, .climo-table td { border: 1px solid #ccc; text-align: center; padding: 10px 2px; font-weight: bold; position: relative; }
        
        /* Force black text for labels */
        .climo-table th, .climo-table td.sticky-col { color: black !important; }
        .sticky-col { position: sticky; left: 0; background-color: #eee !important; z-index: 20; width: 45px; border-right: 2px solid #666 !important; }
        .climo-table thead th { background-color: #ddd !important; z-index: 21; }

        /* Floating Tooltip CSS */
        .climo-table td .tooltiptext {
            visibility: hidden; width: 100px; background-color: #333; color: #fff; text-align: center;
            border-radius: 6px; padding: 5px; position: absolute; z-index: 100; bottom: 125%; left: 50%;
            margin-left: -50px; opacity: 0; transition: opacity 0.2s; font-size: 11px; pointer-events: none;
        }
        .climo-table td:hover .tooltiptext, .climo-table td:active .tooltiptext {
            visibility: visible; opacity: 1;
        }
    </style>
    <div class="scroll-container">
    <table class='climo-table'><thead><tr><th class='sticky-col'>Day</th>""" + "".join(f"<th>{m}</th>" for m in months) + "</tr></thead><tbody>"
    
    for d in range(row_count):
        is_sum = (d == 31)
        html += f"<tr><td class='sticky-col'>{'Sum' if is_sum else d+1}</td>"
        for m in range(12):
            val = v_grid[d][m]
            if val in [999.0, -999.0]: html += "<td>-</td>"; continue
            is_target = (d == yest.day-1 and m == yest.month-1) if mode != "Daily Records" else (d == local_now.day-1 and m == local_now.month-1)
            disp = "T" if val == 0.001 else (f"{val:.2f}" if is_precip else (f"{val:.1f}" if is_snow else f"{int(round(val))}"))
            
            # Add tooltip span inside cell
            tip = str(i_grid[d][m])
            html += f"<td style='{get_style(val, var_key, mode, n_grid[d][m], is_target)}'>{disp}<span class='tooltiptext'>{tip}</span></td>"
        html += "</tr>"
    return html + "</table></div>"

# --- PAGE CONFIG ---
st.set_page_config(page_title="NWS Climate Hub", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stSidebar"] { min-width: 250px; max-width: 80vw; }
    .main .block-container { padding: 1rem !important; }
    .summary-card { background-color: #f8f9fa; padding: 12px; border-radius: 8px; border-left: 5px solid #007bff; margin-bottom: 15px; font-size: 14px; color: black !important; }
    .summary-item { display: inline-block; margin-right: 15px; white-space: nowrap; color: black !important; }
    h1 { font-size: 1.8rem !important; color: inherit; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar UI
state_sel = st.sidebar.selectbox("State", US_STATES, index=US_STATES.index("IL"))
df_stations = get_stations_by_state(state_sel)
site_disp = st.sidebar.selectbox("Station", df_stations['display_name'].tolist()) if not df_stations.empty else st.stop()
selected_site = df_stations[df_stations['display_name'] == site_disp].iloc[0]
mode = st.sidebar.radio("Category", ["Daily Records", "Normals", "YTD Observations", "Departures"])
elem_dict = {"Daily Records": cf.elems_rec, "Normals": cf.elems_avg, "YTD Observations": cf.elems_ytd, "Departures": cf.elems_dep}[mode]
friendly_map = {info['title']: key for key, info in elem_dict.items()}
selected_friendly = st.sidebar.selectbox("Variable", list(friendly_map.keys()))
var_key = friendly_map[selected_friendly]

# Header & Data
st.title(selected_site['name'])
st.caption(f"{selected_friendly} • {mode}")

local_now = get_local_now(state_sel)
target_dt = (local_now - timedelta(days=1)) if mode != "Daily Records" else local_now
summary = get_sidebar_summary(selected_site['sid'], mode, target_dt)

if summary:
    s_html = f"<div class='summary-card'><strong>{target_dt.strftime('%b %d')} Overview:</strong><br>"
    for itm in summary:
        val_s = "Trace" if itm['val'] == 0.001 else (f"{itm['val']:.2f}" if "Precip" in itm['label'] else (f"{itm['val']:.1f}" if "Snow" in itm['label'] else f"{int(round(itm['val']))}"))
        unit = '"' if ("Precip" in itm['label'] or "Snow" in itm['label']) else '°'
        yr = f" ({itm['year']})" if itm.get('year') else ""
        s_html += f"<span class='summary-item'><b>{itm['label']}:</b> {val_s}{unit}{yr}</span>"
    st.markdown(s_html + "</div>", unsafe_allow_html=True)

v, i, n = get_data_grids(selected_site['sid'], var_key, mode, local_now)

if v is not None:
    st.markdown(render_html_table(v, i, n, var_key, mode, local_now), unsafe_allow_html=True)
    st.info("Desktop: Hover for year • Mobile: Tap cell for year")

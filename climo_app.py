import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
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
            por_str = "Unknown"
            vdr = m.get('valid_daterange', [])
            try:
                if vdr and len(vdr) > 0:
                    dates = vdr[0][0]
                    por_str = f"{dates.split('-')[0]}"
            except: por_str = "Unknown"
            entry = {"name": m['name'], "lat": lat, "lon": lon, "por_display": por_str, "sid": thr_sid if thr_sid else icao_sid, "type": "ThreadEx" if thr_sid else "ICAO"}
            if thr_sid: threadex.append(entry)
            else: icao.append(entry)
    df = pd.DataFrame(sorted(threadex, key=lambda x: x['name']) + sorted(icao, key=lambda x: x['name']))
    if not df.empty: df['display_name'] = df.apply(lambda x: f"{x['name']} ({x['sid']})", axis=1)
    return df

# --- DATA FETCHING ---
def get_sidebar_summary(sid, mode, target_date):
    date_str = target_date.strftime("%Y%m%d")
    summary = []

    if mode == "Daily Records":
        config = cf.elems_rec
        por_params = {"sid": sid, "sdate": "por", "edate": "por", "elems": ["maxt", "mint", "pcpn", "snow", "avgt"]}
        por_data = query_acis(por_params)
        if 'data' in por_data:
            target_mmdd = target_date.strftime("%m-%d")
            for i, (key, info) in enumerate(config.items()):
                val_idx = info['val']
                is_high = key in ['maxtmp', 'hmntmp', 'maxpcp', 'maxsnw', 'maxavg']
                day_records = [r for r in por_data['data'] if r[0][5:] == target_mmdd]
                vals = []
                for r in day_records:
                    raw_v = r[val_idx]
                    if raw_v not in ["M", "S", "A"] and "A" not in str(raw_v):
                        v = 0.001 if raw_v == "T" else float(raw_v)
                        vals.append((v, r[0][:4]))
                if vals:
                    v, yr = max(vals) if is_high else min(vals)
                    summary.append({"label": info['title'], "val": v, "year": yr, "unit": info['unit']})
        return summary

    elif mode == "YTD Observations":
        config = cf.elems_ytd
        for key, info in config.items():
            aname = info['aname'].lower()
            if 'pcpn' in aname or 'snow' in aname:
                p = {"sid": sid, "sdate": date_str, "edate": date_str, "elems": [{"name": info['aname'], "duration": "ytd", "reduce": "sum"}]}
            else:
                p = {"sid": sid, "sdate": date_str, "edate": date_str, "elems": [{"name": info['aname']}]}
            res = query_acis(p)
            if 'data' in res and len(res['data']) > 0:
                val = res['data'][0][1] 
                if val not in ["M", "S", "A"]:
                    summary.append({"label": info['title'], "val": float(val) if val != "T" else 0.001, "unit": info.get('unit', 'degrees')})
        return summary

    else:
        if mode == "Normals":
            config, elems = cf.elems_avg, [{"name": e['aname'], "normal": "1"} for e in cf.elems_avg.values()]
        else: # Departures
            config, elems = cf.elems_dep, [{"name": e['aname'], "normal": "departure"} for e in cf.elems_dep.values()]
        data = query_acis({"sid": sid, "sdate": date_str, "edate": date_str, "elems": elems})
        if 'data' in data and data['data']:
            row = data['data'][0]
            for i, (key, info) in enumerate(config.items()):
                try:
                    val = row[i+1]
                    if val not in ["M", "S", "A"]:
                        summary.append({"label": info['title'], "val": float(val) if val != "T" else 0.001, "unit": info.get('unit', 'degrees')})
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
    else: 
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

# --- STYLING & RENDERING ---

def get_style(val, var_key, mode, is_new, is_target, v_grid):
    if val in [999.0, -999.0]: return "background-color: transparent; color: black;"
    if val == 0.001: return "background-color: #ffebcd; color: black;"
    vk = var_key.lower()
    if mode == "Departures":
        if 'pcp' in vk: cmap, norm = cf.brbgcmap, mcolors.Normalize(-1.5, 1.5)
        elif 'snw' in vk: cmap, norm = cf.puorcmap, mcolors.Normalize(-5, 5)
        else: cmap, norm = cf.rdburcmap, mcolors.Normalize(-20, 20)
    else:
        if 'pcp' in vk: cmap, norm = cf.qacmap, mcolors.Normalize(0, 50.0)
        elif 'snw' in vk: cmap, norm = cf.sacmap, mcolors.Normalize(0, 120.0)
        else: cmap, norm = cf.tcmap, mcolors.Normalize(-60, 120)
    rgba = cmap(norm(val))
    style = f"background-color: {mcolors.to_hex(rgba)};"
    if is_new: 
        if ('snw' in vk and val > 0.0) or 'snw' not in vk:
            style += " text-decoration: underline; font-weight: 900; font-size: 1.2em; border: 3px solid black;"
    elif is_target: 
        style += " outline: 3px solid yellow; z-index: 5; position: relative;"
    lum = (0.299*rgba[0] + 0.587*rgba[1] + 0.114*rgba[2])
    style += f" color: {'white' if lum < 0.4 else 'black'};"
    return style

def render_html_table(v_grid, i_grid, n_grid, var_key, mode, local_now):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    yest = local_now - timedelta(days=1)
    vk = var_key.lower()
    is_precip = 'pcp' in vk
    is_snow = any(x in vk for x in ['snw', 'snd', 'snow'])
    row_count = 31 if mode == "Daily Records" else 32

    html = """
    <div class="table-wrapper">
    <style>
        .table-wrapper { 
            overflow-x: auto; 
            -webkit-overflow-scrolling: touch; 
            padding-left: 2px; 
            margin-bottom: 20px;
            border: 1px solid #ccc;
        }
        .climo-table { 
            width: 100%; 
            min-width: 900px; 
            border-collapse: separate; 
            border-spacing: 0; 
            font-size: 18px; 
            table-layout: fixed; 
            color: black;
        }
        .climo-table th, .climo-table td { 
            border-right: 1px solid #ccc; 
            border-bottom: 1px solid #ccc; 
            text-align: center; 
            padding: 8px 0; 
            font-weight: bold; 
        }
        /* Sticky Day Column with Shadow to prevent visual cut-off */
        .label-col { 
            width: 55px; 
            background-color: #eeeeee !important; 
            position: -webkit-sticky;
            position: sticky; 
            left: 0; 
            z-index: 10; 
            border-right: 2px solid #444 !important;
            box-shadow: 2px 0 5px rgba(0,0,0,0.15);
        }
        thead th { 
            position: -webkit-sticky;
            position: sticky; 
            top: 0; 
            background-color: #dddddd !important; 
            z-index: 11; 
        }
        thead th.label-col { z-index: 12; }
        
        .summary-row td { background-color: #f8f8f8; border-top: 2px solid #333; }
        
        @media (max-width: 640px) { 
            .climo-table { font-size: 12px; } 
            .label-col { width: 45px; }
        }
    </style>
    <table class='climo-table'>
    <thead>
        <tr><th class='label-col'>Day</th>""" + "".join(f"<th>{m}</th>" for m in months) + "</tr></thead><tbody>"
    
    for d in range(row_count):
        is_summary_row = (d == 31)
        html += f"<tr class='{'summary-row' if is_summary_row else ''}'><td class='label-col'>{'Avg' if is_summary_row else d+1}</td>"
        for m in range(12):
            val = v_grid[d][m]
            if val in [999.0, -999.0]: 
                html += "<td>-</td>"; continue
            is_target = (d == yest.day-1 and m == yest.month-1) if mode in ["YTD Observations", "Departures"] else (d == local_now.day-1 and m == local_now.month-1)
            disp = "T" if val == 0.001 else (f"{val:.2f}" if is_precip else (f"{val:.1f}" if is_snow else f"{int(round(val))}"))
            html += f"<td title='{i_grid[d][m]}' style='{get_style(val, var_key, mode, n_grid[d][m], is_target, v_grid)}'>{disp}</td>"
        html += "</tr>"
    return html + "</table></div>"

# --- PAGE CONFIG & MAIN UI ---
st.set_page_config(page_title="NWS Climate Hub", layout="wide", initial_sidebar_state="auto")

# UPDATED: Fixes the sidebar width and main content cut-off
st.markdown("""
<style>
    /* Prevent sidebar from squishing main content on narrow screens */
    [data-testid="stSidebar"] { 
        min-width: unset !important; 
        width: 320px; 
    }
    
    /* Ensure main content has enough side padding on mobile */
    .main .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100%;
    }

    .summary-container { display: flex; flex-wrap: wrap; gap: 8px; justify-content: flex-start; margin-top: 10px; }
    .summary-card { background-color: #f1f3f4; border-left: 5px solid #4A90E2; border-radius: 6px; padding: 10px; flex: 1 1 calc(45% - 8px); min-width: 120px; box-shadow: 1px 1px 3px rgba(0,0,0,0.1); }
    .summary-label { font-size: 0.7rem; color: #666; font-weight: bold; display: block; text-transform: uppercase; }
    .summary-value { font-size: 1.1rem; font-weight: 900; color: #111; }
</style>
""", unsafe_allow_html=True)

st.sidebar.header("1. Select Station")
state_sel = st.sidebar.selectbox("State", US_STATES, index=US_STATES.index("IL"))

with st.spinner("Finding stations..."):
    df_stations = get_stations_by_state(state_sel)

if not df_stations.empty:
    site_disp = st.sidebar.selectbox("Location", df_stations['display_name'].tolist())
    selected_site = df_stations[df_stations['display_name'] == site_disp].iloc[0]
    sid = selected_site['sid']
else:
    st.sidebar.error("No sites found."); st.stop()

mode = st.sidebar.selectbox("Category", ["Daily Records", "Normals", "YTD Observations", "Departures"])

elem_dict = {"Daily Records": cf.elems_rec, "Normals": cf.elems_avg, "YTD Observations": cf.elems_ytd, "Departures": cf.elems_dep}[mode]
friendly_map = {info['title']: key for key, info in elem_dict.items()}
selected_friendly = st.sidebar.selectbox("Climate Element", list(friendly_map.keys()))
var_key = friendly_map[selected_friendly]

with st.spinner("Processing..."):
    local_now = get_local_now(state_sel)
    target_dt = (local_now - timedelta(days=1)) if mode in ["YTD Observations", "Departures"] else local_now
    summary = get_sidebar_summary(sid, mode, target_dt)
    
    st.sidebar.markdown(f"--- \n## {target_dt.strftime('%b %d')} Summary")
    summary_html = '<div class="summary-container">'
    for itm in summary:
        lbl = itm['label'].lower()
        val_s, u = ("Trace", "") if itm['val'] == 0.001 else ((f"{itm['val']:.2f}", '"') if "precip" in lbl else ((f"{itm['val']:.1f}", '"') if "snow" in lbl else (f"{int(round(itm['val']))}", "°F")))
        yr_str = f"<br><span style='font-size: 0.7rem; color: #888;'>{itm['year']}</span>" if itm.get('year') else ""
        summary_html += f'<div class="summary-card"><span class="summary-label">{itm["label"]}</span><span class="summary-value">{val_s}{u}</span>{yr_str}</div>'
    summary_html += '</div>'
    st.sidebar.markdown(summary_html, unsafe_allow_html=True)

    v, i, n = get_data_grids(sid, var_key, mode, local_now)
    if v is not None:
        title_suffix = f" (since {selected_site['por_display']})" if mode == "Daily Records" else ""
        st.subheader(f"{selected_friendly} — {selected_site['name']}{title_suffix}")
        st.caption("Swipe left/right to view all months. Underlined cells = Record set this year.")
        st.markdown(render_html_table(v, i, n, var_key, mode, local_now), unsafe_allow_html=True)

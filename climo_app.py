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
            font-size: 15px; 
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

import json
import os
import re
import difflib
import json
from jinja2 import Template
import re
import copy
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from grafana_panel_templates import aliases, PANEL_TEMPLATES



def normalize_chart_type(chart_type: str) -> str:
    available_types = ["stat", "htmlgraphics", "table", "timeseries", "barchart","line"]
    chart_type_clean = chart_type.lower().strip().replace(" ", "").replace("_", "").replace("-", "")
    # print(f"[DEBUG] Normalized: {chart_type} -> {chart_type_clean}")
    if chart_type_clean in aliases:
        resolved = aliases[chart_type_clean]
        # print(f"[DEBUG] Alias resolved: {chart_type_clean} -> {resolved}")
        return resolved
    close_matches = difflib.get_close_matches(chart_type_clean, available_types, n=1, cutoff=0.6)
    if close_matches:
        # print(f"[DEBUG] Close match: {chart_type_clean} -> {close_matches[0]}")
        return close_matches[0]
    # print(f"[DEBUG] Returning raw: {chart_type_clean}")
    return chart_type_clean

def extract_json(text: str) -> str:
    json_match = re.search(r"```json(.*?)```", text, re.DOTALL)
    if json_match:
        return json_match.group(1).strip()
    return text.strip()

def generate_panel_code_from_sql(title: str, sql_query: str, chart_type: str, plt_code: str = None, description: str = None) -> dict:
    chart_type = normalize_chart_type(chart_type)
    if chart_type not in PANEL_TEMPLATES:
        try:
          chart_type=aliases[chart_type]
        except:
          raise ValueError(f"Unsupported chart type: {chart_type}")

    if chart_type == "stat":
        plt_code = None
        sql = re.sub(r'\s+', ' ', sql_query.strip())
        i, depth, count = sql.upper().find("SELECT") + 6, 0, 0

        while i < len(sql):
            if sql[i] == '(': depth += 1
            elif sql[i] == ')': depth -= 1
            elif sql[i:i+3].upper() == 'AS ' and depth == 0:
                count += 1
            i += 1

            if count > 1:
                chart_type = "htmlgraphics"

    panel = copy.deepcopy(PANEL_TEMPLATES[chart_type])
    panel['targets'][0]['rawSql'] = sql_query
    panel['title'] = title
    panel['description'] = description
    # For other chart types, attempt to parse to dict
    # if "\\\\" in panel:
    #         panel = panel.replace("\\\\", "\\")

    try:
        return {
            "panel_code": json.dumps(panel)
        }

    except Exception as e:
        print(f"Error generating panel code: {e}")
        return {
            "panel_code": {}
        }


def extract_chart_type(js_code: str) -> str:
    matches = re.findall(r"type\s*:\s*['\"](\w+)['\"]", js_code, re.IGNORECASE)
    return matches[-1] if matches else ""
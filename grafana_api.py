import requests
import json
import logging
import os
import re
from typing import Dict, List, Optional
from models import db, DashboardHistory
from sqlalchemy import event
from generate_panel_code import generate_panel_code_from_sql

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GrafanaAPI:
    """A class to interact with Grafana's HTTP API."""

    def __init__(self, base_url: str = None, api_key: str = None):
        self.base_url = base_url or os.getenv('GRAFANA_URL', 'http://localhost:3000')
        self.api_key = api_key or os.getenv('GRAFANA_API_KEY')
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def _make_request(self, method: str, endpoint: str, **kwargs) -> dict:
        """Send an HTTP request to the Grafana API."""
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        headers = kwargs.pop('headers', {})
        headers.update(self.headers)

        try:
            response = requests.request(method=method, url=url, headers=headers, **kwargs)
            logger.debug(f"{method} {url} - Status: {response.status_code}")

            if response.status_code >= 400:
                raise requests.HTTPError(f"Grafana API error ({response.status_code}): {response.text}")

            return response.json() if response.text else {}

        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {str(e)}")
            raise

    def create_or_update_dashboard(
        self,
        panel_data: List[dict],
        folder_uid: str = None,
        dashboard_uid: str = None,
        dashboard_title: str = None
    ) -> dict:
        """
        Create or update a single dashboard in Grafana with given panel data.
        Each panel is positioned automatically.
        """
        if not panel_data:
            raise ValueError("No panel data provided")

        if not dashboard_uid:
            raise ValueError("Dashboard UID is required")

        if not dashboard_title:
            dashboard_title = "Untitled Dashboard"

        tags = ['auto-generated']

        try:
            # Initialize dashboard structure
            dashboard = {
                'title': dashboard_title,
                'uid': dashboard_uid,
                'tags': tags,
                'panels': []
            }

            # Loop over panels
            for idx, item in enumerate(panel_data):
                panel_code = generate_panel_code_from_sql(
                    title=item.get('panel_title', 'Untitled Panel'),
                    sql_query=item.get('sql_query', ''),
                    chart_type=item.get('view_type') or item.get('panel_type') or 'table',
                    description=item.get('description', '')
                )

                panel = json.loads(panel_code['panel_code'])

                # Auto layout (2 panels per row)
                panel['gridPos'] = {
                    'x': (idx % 2) * 12,  # two panels per row
                    'y': (idx // 2) * 8,  # each row height 8
                    'w': 12,
                    'h': 8
                }

                dashboard['panels'].append(panel)

            # Build final payload
            dashboard_payload = {
                'dashboard': {
                    'title': dashboard['title'],
                    'uid': dashboard['uid'],
                    'panels': dashboard['panels'],
                    'tags': dashboard['tags'],
                    'timezone': 'browser',
                    'schemaVersion': 36,
                    'version': 0,
                    'refresh': '5m'
                },
                'overwrite': True
            }

            if folder_uid:
                dashboard_payload['folderUid'] = folder_uid

            # Send to Grafana
            result = self._make_request('POST', 'api/dashboards/db', json=dashboard_payload)

            return {
                'status': 'success' if result.get('status') == 'success' else 'error',
                'uid': dashboard_uid,
                'url': result.get('url', f"{self.base_url}/d/{dashboard_uid}"),
                'version': result.get('version', 1),
                'title': dashboard_title
            }

        except Exception as e:
            logger.error(f"Failed to create or update dashboard: {str(e)}")
            return {'error': f"Failed to create or update dashboard: {str(e)}"}

    def export_dashboard_panels(self, dashboard_uid: str) -> List[dict]:
        """Export panels from a dashboard."""
        dashboard = self._make_request('GET', f'api/dashboards/uid/{dashboard_uid}')
        if not dashboard or 'dashboard' not in dashboard:
            raise ValueError(f"Dashboard {dashboard_uid} not found")

        panels = []

        def extract_panels(panel_list):
            for panel in panel_list:
                if 'panels' in panel:  # Nested rows
                    extract_panels(panel['panels'])
                else:
                    sql_query = ''
                    if 'targets' in panel and isinstance(panel['targets'], list):
                        for target in panel['targets']:
                            if 'rawSql' in target:
                                sql_query = target['rawSql']
                                break
                    panels.append({
                        'panel_title': panel.get('title', 'Untitled'),
                        'panel_type': panel.get('type', 'unknown'),
                        'view_type': extract_chart_type(
                            panel.get('options', {}).get('visualEditor', {}).get('code', '')
                        ),
                        'description': panel.get('description', ''),
                        'sql_query': sql_query,
                    })

        extract_panels(dashboard['dashboard'].get('panels', []))
        return panels


def extract_chart_type(js_code: str) -> str:
    """Extract chart type from Grafana panel JavaScript code."""
    matches = re.findall(r"type\s*:\s*['\"](\w+)['\"]", js_code, re.IGNORECASE)
    return matches[-1] if matches else ""


@event.listens_for(DashboardHistory, 'after_insert')
def generate_dashboard_uid(mapper, connection, target):
    """Generate dashboard UID as dashboard_{id} after insert."""
    if not target.dashboard_uid:
        uid = f"dashboard_{target.id}"
        connection.execute(
            DashboardHistory.__table__.update().
            where(DashboardHistory.id == target.id).
            values(dashboard_uid=uid)
        )

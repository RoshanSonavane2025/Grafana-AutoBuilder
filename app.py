import os
import io
import csv
import json
from uuid import uuid4
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
import logging
from models import db, DashboardHistory
from grafana_api import GrafanaAPI

# -------------------- Flask Initialization --------------------
app = Flask(__name__)
CORS(app)

# -------------------- Logging --------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -------------------- Configurations --------------------
app.config.update(
    SQLALCHEMY_DATABASE_URI='sqlite:///grafana_auto_builder.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    UPLOAD_FOLDER='uploads',
    MAX_CONTENT_LENGTH=16 * 1024 * 1024,  # 16 MB
    ALLOWED_EXTENSIONS={'csv'},
    GRAFANA_URL= 'http://localhost:3000',
    GRAFANA_API_KEY='sample_api_key'
)

# Initialize DB
db.init_app(app)
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


# -------------------- Helpers --------------------
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def error_response(message, code=400):
    return jsonify({'error': message}), code


# -------------------- Health Check --------------------
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.1.0'
    }), 200


# -------------------- Dashboard Generator --------------------
@app.route('/api/dashboard/generate', methods=['POST'])
def generate_dashboard():
    """Generate new dashboard from uploaded CSV."""
    file = request.files.get('file')
    folder_uid = request.form.get('folder_uid')
    dashboard_name = request.form.get('dashboardName')
    logger.info(f"Received file: {file.filename}")

    if not file:
        return error_response('No file uploaded')
    if not allowed_file(file.filename):
        return error_response('Invalid file type. Only CSV allowed')
    if not folder_uid:
        return error_response('Folder UID is required')

    try:
        logger.info(f"Processing file: {file.filename}")
        stream = io.StringIO(file.stream.read().decode("utf-8"))
        csv_input = csv.DictReader(stream)
        panel_data = list(csv_input)

        if not panel_data:
            return error_response('CSV file is empty')

        dashboard_uid = f"dashboard_{uuid4().hex[:8]}"
        dashboard_title = dashboard_name if dashboard_name else f"Dashboard {uuid4().hex[:8]}"

        grafana = GrafanaAPI(api_key=app.config['GRAFANA_API_KEY'], base_url=app.config['GRAFANA_URL'])
        logger.info(f"Creating dashboard: {dashboard_title}")
        result = grafana.create_or_update_dashboard(panel_data, folder_uid, dashboard_uid, dashboard_title)

        # Save to DB
        if result.get('error'):
            return error_response(result['error'], 500)
        history = DashboardHistory.query.filter_by(dashboard_uid=dashboard_uid).first()
        if not history:
            history = DashboardHistory(
                dashboard_uid=dashboard_uid,
                dashboard_title=dashboard_title,
                folder_uid=folder_uid,
                panel_count=len(panel_data)
            )
            db.session.add(history)
        else:
            history.updated_at = datetime.utcnow()
            history.panel_count = len(panel_data)

        db.session.commit()
        logger.info(f"Dashboard created: {dashboard_title}")
        return jsonify({
            'status': 'success',
            'dashboard_uid': dashboard_uid,
            'dashboard_title': dashboard_title,
            'folder_uid': folder_uid,
            'panel_count': len(panel_data),
            'url': f"{app.config['GRAFANA_URL']}/d/{dashboard_uid}"
        }), 201

    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Error generating dashboard: {str(e)}")
        return error_response(str(e), 500)


# -------------------- Dashboard History --------------------
@app.route('/api/dashboard/history', methods=['GET'])
def get_dashboard_history():
    try:
        dashboards = DashboardHistory.query.order_by(DashboardHistory.updated_at.desc()).all()
        return jsonify([d.to_dict() for d in dashboards]), 200
    except Exception as e:
        app.logger.error(f"Error fetching dashboard history: {str(e)}")
        return error_response('Failed to fetch dashboard history', 500)


# -------------------- Dashboard Export --------------------
@app.route('/api/dashboard/export', methods=['GET'])
def export_dashboard():
    dashboard_uid = request.args.get('uid')
    export_format = request.args.get('format', 'json').lower()

    if not dashboard_uid:
        return error_response('Dashboard UID is required')
    if export_format not in ['csv', 'json']:
        return error_response('Invalid format. Use csv or json')

    try:
        grafana = GrafanaAPI(api_key=app.config['GRAFANA_API_KEY'], base_url=app.config['GRAFANA_URL'])
        panels = grafana.export_dashboard_panels(dashboard_uid)

        if not panels:
            return error_response('No panels found', 404)

        if export_format == 'csv':
            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=panels[0].keys())
            writer.writeheader()
            writer.writerows(panels)

            return app.response_class(
                output.getvalue(),
                mimetype='text/csv',
                headers={
                    'Content-Disposition': f'attachment;filename={dashboard_uid}_panels.csv'
                }
            )
        else:
            return jsonify({
                'dashboard_uid': dashboard_uid,
                'panel_count': len(panels),
                'panels': panels
            }), 200

    except Exception as e:
        app.logger.error(f"Error exporting dashboard {dashboard_uid}: {str(e)}")
        return error_response(str(e), 500)


@app.route('/api/settings', methods=['POST'])
def update_settings():
    data = request.get_json()
    api_key = data.get('grafanaKEY')
    base_url = data.get('grafanaURL')

    if not api_key or not base_url:
        return jsonify({'error': 'API key and Grafana URL are required'}), 400

    app.config['GRAFANA_API_KEY'] = api_key
    app.config['GRAFANA_URL'] = base_url

    return jsonify({'status': 'success', 'message': 'Settings updated successfully'}), 200


@app.route('/api/current_settings', methods=['GET'])
def get_current_settings():
    key = app.config.get('GRAFANA_API_KEY', '')
    masked_key = key[:6] + '****' if key else ''
    return jsonify({
        'grafanaURL': app.config.get('GRAFANA_URL', ''),
        'grafanaKEY': masked_key
    }), 200


# -------------------- Frontend Route --------------------
@app.route('/')
def index():
    return render_template('grafana_dashboard_system.html')




# -------------------- Main Entry --------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

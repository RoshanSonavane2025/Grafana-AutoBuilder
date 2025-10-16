# Grafana Dashboard Automation System

A Flask-based backend system for automating Grafana dashboard creation, management, and export. This system allows you to programmatically generate Grafana dashboards from CSV files, track dashboard history, and export dashboard configurations.

## Features

- **Dashboard Generation**: Create Grafana dashboards from CSV files
- **Dashboard History**: Track all created dashboards with metadata
- **Panel Export**: Export dashboard panels to CSV or JSON format
- **RESTful API**: Well-documented API endpoints for integration
- **Database Backed**: PostgreSQL database for storing dashboard history

## Prerequisites

- Python 3.8+
- PostgreSQL
- Grafana instance (local or remote)
- Grafana API key with admin privileges

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd GrafanaAutoBuilder
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Copy the example environment file and update with your configuration:
   ```bash
   cp .env.example .env
   ```
   Edit the `.env` file with your Grafana and database details.

5. **Initialize the database**
   ```bash
   flask db upgrade
   ```

## Running the Application

1. **Start the development server**
   ```bash
   flask run
   ```
   The application will be available at `http://localhost:5000`

2. **For production**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

## API Documentation

### Health Check
- **GET** `/api/health`
  Check if the API is running.

### Dashboard Generation
- **POST** `/api/dashboard/generate`
  Generate a new dashboard from a CSV file.
  
  **Form Data**:
  - `file`: CSV file with panel definitions
  - `folder_uid`: Target Grafana folder UID

### Dashboard History
- **GET** `/api/dashboard/history`
  Get history of all created dashboards.

### Export Dashboard
- **GET** `/api/dashboard/export`
  Export dashboard panels.
  
  **Query Parameters**:
  - `uid`: Dashboard UID (required)
  - `format`: Output format (`csv` or `json`, default: `json`)

## CSV Format

The CSV file should have the following columns:
- `dashboard_name`: Name of the dashboard
- `title`: Panel title
- `sql_query`: SQL query for the panel
- `chart_type`: Type of chart (e.g., 'timeseries', 'bar', 'pie', 'stat')
- `description`: (Optional) Panel description
- `tags`: (Optional) Comma-separated list of tags

Example:
```csv
dashboard_name,title,sql_query,chart_type,description,tags
Sales Dashboard,Monthly Sales,SELECT date_trunc('month', order_date) as time, sum(amount) as sales FROM orders GROUP BY 1,timeseries,Monthly sales data,"sales, revenue"
Sales Dashboard,Top Products,SELECT product_name, sum(quantity) as total_quantity FROM order_items GROUP BY product_name ORDER BY total_quantity DESC LIMIT 5,bar,Top selling products,
```

## Project Structure

```
GrafanaAutoBuilder/
├── app.py                 # Main application file
├── grafana_api.py         # Grafana API client
├── generate_panel_code.py # Panel code generation
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment variables
├── static/                # Static files (CSS, JS)
│   ├── scripts.js
│   └── styles.css
└── templates/             # HTML templates
    └── grafana_dashboard_system.html
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

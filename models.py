from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import uuid
db = SQLAlchemy()

class DashboardHistory(db.Model):
    """Model to track dashboard creation history."""
    __tablename__ = 'dashboard_history'
    
    id = db.Column(db.Integer, primary_key=True)
    dashboard_uid = db.Column(db.String(100), nullable=False, unique=True)
    dashboard_title = db.Column(db.String(255), nullable=False)
    folder_uid = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    panel_count = db.Column(db.Integer, default=0)
    
    def to_dict(self):
        """Convert model to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'dashboard_uid': self.dashboard_uid,
            'dashboard_title': self.dashboard_title,
            'folder_uid': self.folder_uid,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'panel_count': self.panel_count
        }

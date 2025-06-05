from app import app, db
from app.models import Todo
from datetime import datetime

with app.app_context():
    db.create_all()
    print("Database tables created successfully!") 
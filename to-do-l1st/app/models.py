from app import db
from datetime import datetime, UTC

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)
    date = db.Column(db.Date, default=datetime.now(UTC))
    
    def __repr__(self):
        return self.text
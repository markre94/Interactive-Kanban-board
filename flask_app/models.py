from flask_app import db
from datetime import datetime
from sqlalchemy import Enum


class Task(db.Model):
    """Task class
    Attributes:
        id (int): Unique id, primary key, auto increment.
        username (str): Foreign key referencing Users table.
        task (str): Details of the task.
        status (enum): Status of the task, with the following values
            - 'to_do'
            - 'doing'
            - 'done'
    """

    id = db.Column(db.Integer, primary_key=True)
    # username = db.relationship('User')
    content = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(Enum('to_do', 'doing', 'done'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f"User ('{self.login}')"

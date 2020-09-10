from datetime import datetime
from sqlalchemy import Enum
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin

login_manager = LoginManager()
db = SQLAlchemy()


@login_manager.user_loader
def load_eser(user_id):
    return User.query.get(int(user_id))


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
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String)
    tasks = db.relationship('Task', backref='owner')

    def __repr__(self):
        return f"User ('{self.login}')"

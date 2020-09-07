from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_app.forms import RegistrationFrom, LoginFrom
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config ["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
db = SQLAlchemy(app)
app.config ['SECRET_KEY'] = 'ZOMn8n1Jt8KTfXPwbcZ3tw'
bcrypt = Bcrypt(app)

from flask_app import views, auth_views
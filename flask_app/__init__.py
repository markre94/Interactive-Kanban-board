from flask import Flask
from flask_app.forms import RegistrationFrom, LoginFrom
from flask_bcrypt import Bcrypt
from flask_app.models import db, login_manager

app = Flask(__name__)
app.config ["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
app.config ['SECRET_KEY'] = 'ZOMn8n1Jt8KTfXPwbcZ3tw'
bcrypt = Bcrypt(app)
db.init_app(app)

login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'



from flask_app import views, auth_views
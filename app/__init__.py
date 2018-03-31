from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import MySQLdb

HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'ultimate_meal_planner'



app = Flask(__name__)
app.config['SECRET_KEY'] = 'THIS IS THE BEST KEY I EVER HAD'
#mysql = MySQLdb.connect(HOST, USER, PASSWORD ,DATABASE)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/"+DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'gif','png'])
db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # necessary to tell Flask-Login what the default route is for the login page
login_manager.login_message_category = "info"  # customize the flash message category

app.config.from_object(__name__)
from app import views

"""
Copyright 2018-2020 AutomizeApps Inc. All Rights Reserved.

Codebase Contributed by:
Author 1: Tarun Singh <thetseffect@gmail.com> (24 Jul,2019 to 24th Nov,2019)
Author 2: Pratik Rane <pratikrane149@gmail.com> (24th Nov,2019 to 24 Feb,2020)
Author 3: Vikas Donthula <donthulavikas1999@gmail.com> (DD Feb,2020 to DD MMM, YYYY)
"""

from flask import Flask, Response
from flask_basicauth import BasicAuth
from flask_cors import CORS
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from werkzeug.exceptions import HTTPException
from flask_login import LoginManager
from itsdangerous import URLSafeSerializer
#import psycopg2
import warnings
warnings.filterwarnings("ignore")


"""
These Try blocks checks whether the required nltk dependencies are installed in the system or not.
If not found, then by running its respective except block, they are downloaded and installed.

NOTICE:
In future if more nltk dependencies are going to be used in this app,
then it is recommended to add a try/except block for the same.

Otherwise, when deployed on server, the dependency might not get installed,
which may prone into 500 server error page. 
"""
# Initializing Flask App
app = Flask(__name__)

# Loading all configuration variables depending on environment from config.py
if app.config["ENV"] == "development":
	app.config.from_object("config.DevelopmentConfig")
else:
    app.config.from_object("config.ProductionConfig")

# This video demonstrates why we use CORS in our Flask App - https://www.youtube.com/watch?v=vWl5XcvQBx0
CORS(app)

# This setting helps us to use zip() in jinja2 templates
app.jinja_env.globals.update(zip=zip)

# This is the configuration settings for generating the log of our app (deprecated)
# logging.basicConfig(filename='ReviewsCruncher.log', level=logging.DEBUG, format='%(asctime)s  %(levelname)s  %(name)s  %(thread)d  : %(message)s')


class SQLAlchemy(_BaseSQLAlchemy):
	"""
	This class is defined so that we can set "pool_pre_ping" to True.
	pool_pre_ping is a boolean flag, which when set to True,
	will enable the connection pool 'pre-ping' feature
	that tests connections for liveness upon each checkout.
	
	This prevents from dropping of database connection with our app.

	This class inherits the original SQLAlchemy class,
	and nothing else is changed except pool_pre_ping flag

	https://docs.sqlalchemy.org/en/13/core/pooling.html#dealing-with-disconnects
	https://github.com/pallets/flask-sqlalchemy/issues/589
	"""
	def apply_pool_defaults(self, app, options):
		super(SQLAlchemy, self).apply_pool_defaults(app, options)
		options["pool_pre_ping"] = True

# Creating and Initializing db object of SQLAlchemy class
db = SQLAlchemy(app)
db.init_app(app)

migrate = Migrate(app, db, render_as_batch=True)

with app.app_context():
	if db.engine.url.drivername == 'sqlite':
		migrate.init_app(app, db, render_as_batch=True)
	else:
		migrate.init_app(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)


"""
Creating basic_auth object of BasicAuth class.
We are using BasicAuth only to protect our Admin pages.

WARNING:
We implemented BasicAuth when this App was in early stage.
This is not a full-fledged authentication and
authorization system for our admin panel.

It is recommended to replace BasicAuth with a
proper authentication system using Flask-Login,
the way we have for our client users.
"""
basic_auth = BasicAuth(app)

# Creating serializer object of URLSafeSerializer class for serializing session_token
serializer = URLSafeSerializer(app.secret_key)

# Creating login_manager object of LoginManager class for implementing Flask-Login
login_manager = LoginManager(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(int(user_id))
    except ValueError:
        return None


"""
The following three classes are inherited from their respective base class,
and are customized, to make flask_admin compatible with BasicAuth.

The following link described the problem and solution.
https://stackoverflow.com/questions/54834648/flask-basicauth-auth-required-decorator-for-flask-admin-views
"""
class AuthException(HTTPException):
	def __init__(self, message):
		super().__init__(message, Response(
			"You could not be authenticated. Please refresh the page.", 401,
			{'WWW-Authenticate': 'Basic realm="Login Required"'} ))

class MyModelView(ModelView):
	def is_accessible(self):
		if not basic_auth.authenticate():
			raise AuthException('Not authenticated.')
		else:
			return True
	def inaccessible_callback(self, name, **kwargs):
		return redirect(basic_auth.challenge())

class MyAdminIndexView(AdminIndexView):
	def is_accessible(self):
		if not basic_auth.authenticate():
			raise AuthException('Not authenticated.')
		else:
			return True
	def inaccessible_callback(self, name, **kwargs):
		return redirect(basic_auth.challenge())

# Creating admin object of Admin class to implement flask_admin
admin = Admin(app, index_view=MyAdminIndexView(url='/kUQqQm9geK'), name='Admin', template_mode='bootstrap3')


# Importing models from models.py to register them on Admin Panel
from reviewcruncher.models import User, CustomizationOfFeatures

"""
Here we register our models using add_view method so that,
the database tables can be viewed from Flask Admin Panel.

If any new models are created then it is recommended to import them,
and then register them here, so that the Admin can view them in Admin Panel
"""
# admin.add_view(MyModelView(Company, db.session, category='Database Overview'))
admin.add_view(MyModelView(User, db.session, category='Database Overview'))
admin.add_view(MyModelView(CustomizationOfFeatures, db.session, category='Database Overview'))

"""
Here we import our blueprints and register them using
register_blueprint method, so that the routes defined in
respective blueprint packages can be accessed from here.

If any new blueprint packages are created then it is required
to import and register them here.
"""
from reviewcruncher.admin.views import myadmin
from reviewcruncher.client.views import client

app.register_blueprint(myadmin, url_prefix='/kUQqQm9geK')
app.register_blueprint(client)

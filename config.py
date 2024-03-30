import os

class BaseConfig(object):
	"""
	Use this class to share any default attributes with any subsequent
	classes that inherit from BaseConfig.
	"""
	DEBUG = False

	# Generated with secrets.token_hex(16)
	SECRET_KEY = "2b5ad098aac8403c8464d212e404f5e1"
	
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_ECHO = False

	# Flask-Admin theme
	FLASK_ADMIN_SWATCH = "flatly"
	
	# All paths used in App 
	MAIN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
	CLIENT_DIR = os.path.join(MAIN_DIR, 'client')
	BASE_DIR = os.path.join( os.path.dirname(os.path.realpath(__file__)), 'reviewcruncher')
	CSV_DIR = os.path.join(BASE_DIR,'input_files','CSVs')
	WORDCLOUD_DIR = os.path.join(BASE_DIR,'static','wordclouds')
	MAP_DIR = os.path.join(BASE_DIR,'templates','maps')
	PRICING=os.path.join(BASE_DIR,'Retailer_Pricing.csv')
	BEST=os.path.join(BASE_DIR,'Bestseller.csv')
	SEARCH=os.path.join(BASE_DIR,'Search.csv')
	PRODUCT_INFO = os.path.join(BASE_DIR,'admin','utils','PRODUCT_INFO_client.csv')
	ALLOWED_FILE_EXTENSIONS = ["CSV"]

class ProductionConfig(BaseConfig):
	SECRET_KEY = "ed08e11c1b61624f465cc72302eea01e"
	SQLITE_DB_DIR = os.path.join( os.path.dirname(os.path.realpath(__file__)), 'db.sqlite')
	SQLALCHEMY_DATABASE_URI = "sqlite:///"+SQLITE_DB_DIR

	BASIC_AUTH_USERNAME = "admin"
	BASIC_AUTH_PASSWORD = "main-admin@123"
	BASIC_AUTH_FORCE = False

class DevelopmentConfig(BaseConfig):
	# DEBUG = False
	SECRET_KEY = "7e20c2699c1d144cacc81da1ee79acf0"
	SQLITE_DB_DIR = os.path.join( os.path.dirname(os.path.realpath(__file__)), 'db.sqlite')
	SQLALCHEMY_DATABASE_URI = "sqlite:///"+SQLITE_DB_DIR
	# SQLALCHEMY_ECHO = False

	BASIC_AUTH_USERNAME = "admin"
	BASIC_AUTH_PASSWORD = "main-admin@123"
	BASIC_AUTH_FORCE = False

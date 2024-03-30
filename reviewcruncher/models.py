from reviewcruncher import db
from flask_login import UserMixin
 
class Service(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	company_name = db.Column(db.String(100), unique=True, nullable=False)
 
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(100), unique=True, nullable=False)
    company = db.Column(db.String(100), nullable=False)
    pdfs = db.relationship('PDF', backref='category', lazy=True)

class PDF(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    publisher = db.Column(db.String(255), nullable=False)
    language = db.Column(db.String(50), nullable=False)
    service_name = db.Column(db.String(50), nullable=False)
    pdf_file = db.Column(db.String(255), nullable=False)
    image_file = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)
	phone = db.Column(db.String(20))
	password = db.Column(db.String(255), nullable=False)

class CustomizationOfFeatures(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	company_name=db.Column(db.Text)
	maps = db.Column(db.Boolean)
	wordcloud = db.Column(db.Boolean)
	sentiment = db.Column(db.Boolean)
	features = db.Column(db.Boolean)
	topics = db.Column(db.Boolean)
	competitor = db.Column(db.Boolean)
	retailanalysis = db.Column(db.Boolean)
	pricing = db.Column(db.Boolean)
	bestseller=db.Column(db.Boolean)
	sales=db.Column(db.Boolean)
	market_share=db.Column(db.Boolean)
	search=db.Column(db.Boolean)
	company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete='CASCADE',name='fk'), nullable=False)
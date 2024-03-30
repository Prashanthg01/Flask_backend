from flask import render_template, url_for, request, redirect, flash, jsonify
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import check_password_hash
from reviewcruncher.models import User
from werkzeug.security import generate_password_hash
from reviewcruncher import db, app
from reviewcruncher.client.views import client
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

#Custom Directories
CSV_DIR = app.config['CSV_DIR']
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@client.route('/')
def index():
	return jsonify({'heading': "Wellcom, you are in main page"})

@client.errorhandler(500)
def internal_error(error):
	db.session.rollback()
	return render_template('client/dashboard/500.html'), 500

@client.errorhandler(404)
def not_found_error(error):
	return render_template('client/dashboard/404.html'), 404


@client.route('/home', methods=['GET'])
@login_required
def home():
    heading = 'Welcome back!'
    text = 'You are in the Home page'
    return jsonify({'heading': heading, 'text': text})


@client.route('/register', methods=['GET', 'POST'])
def register():
    data = request.get_json()
    print(data)
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(name=data['name'], email=data['email'], phone=data['phone'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

@client.route('/login', methods=['GET', 'POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@client.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'})

# Required for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# from flask import render_template, url_for, request, redirect, flash
# from werkzeug.security import generate_password_hash
# from reviewcruncher.models import User, CustomizationOfFeatures, Category, Service
# from reviewcruncher import db, basic_auth, app
# import os
# import shutil

# from reviewcruncher.admin.views import myadmin

# # These are the custom required paths which are defined in config.py
# CSV_DIR = app.config['CSV_DIR']
# WORDCLOUD_DIR = app.config['WORDCLOUD_DIR']
# MAP_DIR = app.config['MAP_DIR']
# BASE_DIR=app.config['BASE_DIR']

# # @myadmin.route('/register_company', methods=['GET','POST'])
# # @basic_auth.required
# # def register_company():
# # 	if request.method=='POST':
# # 		# Here we fetch the form data.
# # 		company_name = request.form.get('company_name')
# # 		company = Service.query.filter_by(company_name=company_name).first()

# # 		if company:
# # 			flash('Company with this name already exists')
# # 			return redirect(url_for('myadmin.register_company'))
# # 		else:
# # 			new_company = Service(company_name=company_name)
# # 			db.session.add(new_company)
# # 			db.session.commit()

# # 			company_csv_dir = os.path.join(CSV_DIR, company_name)
# # 			os.makedirs(company_csv_dir, exist_ok=True) # Create folder to store PRODUCT_*.csv and FEATURE_*.csv
			
# # 			flash('Company has been successfully registered, and all its neccessary folders have been created!')
# # 			return redirect(url_for('admin.index'))

# # 	# GET method:
# # 	return render_template('admin/registration/register_company.html')

# @myadmin.route('/register_category', methods=['GET', 'POST'])
# @basic_auth.required
# def register_category():
#     category_name = request.form.get('category_name')
#     company = request.form.get('company')
#     company_remove = request.form.get('company_remove')
#     category_name_remove = request.form.get('category_name_remove')

#     if category_name and company:
#         category = Category.query.filter_by(category_name=category_name).first()

#         if category:
#             flash('Category with this name already exists')
#             return redirect(url_for('myadmin.register_company'))
#         else:
#             new_category = Category(category_name=category_name, company=company)
#             db.session.add(new_category)
#             db.session.commit()

#             company_csv_dir = os.path.join(CSV_DIR, company, category_name)
#             os.makedirs(company_csv_dir, exist_ok=True)  # Create folder to store PRODUCT_*.csv and FEATURE_*.csv
#             os.makedirs(os.path.join(CSV_DIR, company, category_name, "PDFs"), exist_ok=True) 
#             os.makedirs(os.path.join(BASE_DIR, "static", "img", company), exist_ok=True) 

#             flash('Category has been successfully registered, and all its necessary folders have been created!')
#             return redirect(url_for('admin.index'))

#     elif company_remove and category_name_remove:
#         # Remove the category and its associated folder
#         category_to_remove = Category.query.filter_by(company=company_remove, category_name=category_name_remove).first()

#         if category_to_remove:
#             db.session.delete(category_to_remove)
#             db.session.commit()

#             company_csv_dir_to_remove = os.path.join(CSV_DIR, company_remove, category_name_remove)
#             shutil.rmtree(company_csv_dir_to_remove, ignore_errors=True)  # Remove the folder

#             flash('Category has been successfully removed, and its associated folder has been deleted!')
#             return redirect(url_for('admin.index'))
#         else:
#             flash('Category not found for removal')
#             return redirect(url_for('admin.index'))

#     # GET method:
#     company_dropdown_options = []
#     companies = Service.query.all()
#     for company in companies:
#         company_dropdown_options.append(company.company_name)
        
#     category_dropdown_options = []
#     categorys = Category.query.all()
#     for category in categorys:
#         category_dropdown_options.append(category.category_name)

#     return render_template('admin/registration/register_category.html', company_dropdown_options=company_dropdown_options, category_dropdown_options=category_dropdown_options)

# @myadmin.route('/register_user', methods=['GET','POST'])
# @basic_auth.required
# def register_user():
# 	"""
# 	Route for registering client user.

# 	GET method: if request method is GET then it serves and renders
# 	a template, with a list of company names to populate them in dropdown.
	
# 	POST method: if request method is POST then it registers a user,
# 	if it doesn't already exist.
# 	"""

# 	# POST method:
# 	if request.method == 'POST':
# 		# Here we fetch the form data.
# 		email = request.form.get('email')
# 		name = request.form.get('name')
# 		company = 'LIS Academy Digital Portal'
# 		phone = request.form.get('phone')
# 		password1 = request.form.get('password1')
# 		password2 = request.form.get('password2')
		
# 		# if this query returns a user, then email already exists in database.
# 		user = User.query.filter_by(email=email).first()
		
# 		if user:
# 			# if a user is found, we will redirect back to signup page.
# 			flash('Email address already exists')
# 			return redirect(url_for('myadmin.register_user'))

# 		if password1 and password2 and password1 != password2:
# 			flash('Password did not match. Please try again.')
# 			return redirect(url_for('myadmin.register_user'))

# 		company_obj = Company.query.filter_by(company_name=company).first()
# 		# Create new user with the form data, and add it to the database.
# 		new_user = User(email=email,name=name, phone=phone, company=company,
# 						password=generate_password_hash(password2, method='sha256'),
# 						company_user=company_obj)
# 		db.session.add(new_user)
# 		db.session.commit()

# 		flash('Account has been successfully created!')
# 		return redirect(url_for('admin.index'))

# 	# GET method:
# 	company_dropdown_options = []
# 	companies = Company.query.all()
# 	for company in companies:
# 		company_dropdown_options.append(company.company_name)
# 	return render_template('admin/registration/register_user.html', company_dropdown_options=company_dropdown_options)

# ###### new code #######
# @myadmin.route('/customize_features', methods=['GET', 'POST'])
# @basic_auth.required
# def customize_features():
#     complete_data = CustomizationOfFeatures.query.all()
#     existing_record = None
#     existing_data = None

#     companies = Company.query.all()
#     company_dropdown_options = [company.company_name for company in companies]
#     company = request.form.get('company')
#     company = company
#     if company:
#         existing_data = CustomizationOfFeatures.query.filter_by(company_name=company).first()
        
#     company_name = request.form.get('company_name')
#     company_data = Company.query.filter_by(company_name=company_name).first()
#     if company_data:
#         company_id = company_data.id
#         action = request.form.get('action')

#         if action == 'customize':
#             existing_record = CustomizationOfFeatures.query.filter_by(company_name=company_name).first()

#             if existing_record:
#                 existing_record.wordcloud = request.form.get('wordcloud') == '1'
#                 existing_record.sentiment = request.form.get('sentiment') == '1'
#                 existing_record.features = request.form.get('features') == '1'
#                 existing_record.competitor = request.form.get('competitor') == '1'
#                 existing_record.retailanalysis = request.form.get('retailanalysis') == '1'
#                 existing_record.maps = request.form.get('maps') == '1'
#                 existing_record.market_share = request.form.get('market_share') == '1'
#                 existing_record.bestseller = request.form.get('bestseller') == '1'
#                 existing_record.pricing = request.form.get('pricing') == '1'
#                 existing_record.sales = request.form.get('sales') == '1'
#                 existing_record.search = request.form.get('search') == '1'
#                 existing_record.topics = request.form.get('topics') == '1'
#                 db.session.commit()
#                 flash('Company features have been updated successfully!')
#             else:
#                 new_record = CustomizationOfFeatures(
#                     company_name=company_name,
#                     wordcloud=request.form.get('wordcloud') == '1',
#                     company_id=company_id,
#                     sentiment=request.form.get('sentiment') == '1',
#                     features=request.form.get('features') == '1',
#                     competitor=request.form.get('competitor') == '1',
#                     retailanalysis=request.form.get('retailanalysis') == '1',
#                     maps=request.form.get('maps') == '1',
#                     market_share=request.form.get('market_share') == '1',
#                     bestseller=request.form.get('bestseller') == '1',
#                     pricing=request.form.get('pricing') == '1',
#                     sales=request.form.get('sales') == '1',
#                     search=request.form.get('search') == '1',
#                     topics=request.form.get('topics') == '1'
#                 )
#                 db.session.add(new_record)
#                 db.session.commit()

#                 flash('Company has been successfully registered, and all its necessary folders have been created!')

#             return redirect(url_for('myadmin.customize_features'))
#         ### Delete existing record ###
#         elif action == 'delete':
#             existing_record = CustomizationOfFeatures.query.filter_by(company_name=company_name).first()

#             if existing_record:
#                 db.session.delete(existing_record)
#                 db.session.commit()
#                 flash('Company features have been deleted successfully!')
#             else:
#                 flash('No customization record found for this company.')

#     company_dropdown_options = [company.company_name for company in Company.query.all()]
#     return render_template('admin/registration/customize_features.html', company_dropdown_options=company_dropdown_options, company = company, complete_data=complete_data, existing_record=existing_record, existing_data=existing_data)
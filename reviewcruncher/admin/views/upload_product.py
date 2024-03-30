# import os
# from flask import render_template, url_for, request, redirect, flash
# from reviewcruncher import basic_auth, app
# from reviewcruncher.models import Company, Category, db, PDF, Service, User
# from werkzeug.utils import secure_filename
# from reviewcruncher.admin.views import myadmin

# # These are the custom required paths which are defined in config.py
# CSV_DIR = app.config['CSV_DIR']
# WORDCLOUD_DIR = app.config['WORDCLOUD_DIR']
# MAP_DIR = app.config['MAP_DIR']
# BASE_DIR=app.config['BASE_DIR']
# ALLOWED_FILE_EXTENSIONS = app.config["ALLOWED_FILE_EXTENSIONS"]

# def allowed_file(filename):
# 	if not "." in filename: # We only want files with a . in the filename
# 		return False

# 	ext = filename.rsplit(".", 1)[1] # Split the extension from the filename
# 	if ext.upper() in ALLOWED_FILE_EXTENSIONS: # Check if the extension is in ALLOWED_FILE_EXTENSIONS
# 		return True
# 	else:
# 		return False

# @myadmin.route('/upload_multiple_files', methods=['GET', 'POST'])
# @basic_auth.required
# def upload_multiple_files():
#     # POST method:
#     if request.method == "POST":
#         if request.files:
#             company = request.form.get('company')
#             category = request.form.get('category')
#             files = request.files.getlist('files[]')

#             for csv_file in files:
#                 if csv_file and allowed_file(csv_file.filename):
#                     app.logger.info("Updating file: " + str(csv_file))
#                 if csv_file.filename == "":  # Make sure that the filename is not an empty string.
#                     flash("No filename")
#                     return redirect(url_for('myadmin.upload_multiple_files'))
#                 else:  # If all above conditions are satisfied then the file is uploaded.
#                     try:
#                         filename = csv_file.filename
#                         csv_file.save(os.path.join(CSV_DIR, company, category, filename))
#                         flash(filename + " file uploaded successfully!")

#                     except FileNotFoundError as e:
#                         flash("Name of the uploaded file is too long. Try shortening it.")
#                         return redirect(url_for('myadmin.upload_multiple_files'))
#     # GET method:
#     company_dropdown_options = []
#     companies = Company.query.all()
#     for company in companies:
#         company_dropdown_options.append(company.company_name)

#     category_dropdown_options = []
#     categorys = Category.query.all()
#     for category in categorys:
#         category_dropdown_options.append(category.category_name)
        
#     return render_template("admin/add_product/upload_file.html", company_dropdown_options=company_dropdown_options, category_dropdown_options=category_dropdown_options)

# @myadmin.route('/add_category', methods=['GET', 'POST'])
# @basic_auth.required
# def add_category():
#     if request.method == 'POST':
#         category_name = request.form.get('category_name')
#         company = request.form.get('company')

#         # Check if the category name already exists
#         existing_category = Category.query.filter_by(category_name=category_name).first()
#         if existing_category:
#             # Handle case where category name already exists
#             return render_template('admin/add_product/add_category.html', error='Category name already exists.')

#         # Create a new category
#         new_category = Category(category_name=category_name, company=company)
#         db.session.add(new_category)
#         db.session.commit()

#         # Redirect to a success page or the category list page
#         return redirect(url_for('myadmin.add_category'))

#     return render_template('admin/add_product/add_category.html')

# @myadmin.route('/get_service_data', methods=['GET', 'POST'])
# @basic_auth.required
# def get_service_data():
#     service_name = request.form.get('service_name')
#     print(service_name)
#     return redirect(url_for('myadmin.add_pdf', service_name=service_name))

# @myadmin.route('/add_pdf', methods=['GET', 'POST'])
# @basic_auth.required
# def add_pdf():
#     service_name = None
#     service_name = request.args.get('service_name')
#     categories = Category.query.filter_by(company=service_name).all() if service_name else Category.query.all()
#     if request.method == 'POST':
#         title = request.form.get('title')
#         author = request.form.get('author')
#         publisher = request.form.get('publisher')
#         language = request.form.get('language')
#         category_name = request.form.get('category_name')
#         service_name = request.form.get('service_name')
#         pdf_file = request.files['pdf_file']
#         image_file = request.files['image_file']
        
#         print(service_name, category_name)

#         # Find or create the category
#         category = Category.query.filter_by(category_name=category_name).first()
#         if not category:
#             category = Category(category_name=category_name, company="Your Company")
#             db.session.add(category)
#             db.session.commit()

#         # Save the uploaded files
#         pdf_file_path = os.path.join(CSV_DIR, service_name, category_name, "PDFs", secure_filename(pdf_file.filename))
#         image_file_path = os.path.join(BASE_DIR, "static", "img", service_name, secure_filename(image_file.filename))
#         print(image_file_path)
#         pdf_file.save(pdf_file_path)
#         image_file.save(image_file_path)

#         # Create a new PDF entry
#         pdf = PDF(
#             title=title,
#             author=author,
#             publisher=publisher,
#             language=language,
#             service_name=service_name,
#             pdf_file=os.path.join(secure_filename(pdf_file.filename)),
#             image_file=os.path.join(secure_filename(image_file.filename)),
#             category_id=category.id
#         )

#         db.session.add(pdf)
#         db.session.commit()

#         return redirect(url_for('myadmin.add_pdf'))

#     Services = Service.query.all()
#     return render_template('admin/add_product/add_pdf.html', categories=categories, Services=Services, service_name=service_name)

# @myadmin.route('/over_view', methods=['GET', 'POST'])
# @basic_auth.required
# def over_view():
#     total_users = User.query.count()
#     total_pdf = PDF.query.count()
#     return render_template('admin/add_product/overview.html', total_users=total_users, total_pdf=total_pdf)
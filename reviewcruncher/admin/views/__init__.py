from flask import Blueprint

myadmin = Blueprint('myadmin', __name__)

from reviewcruncher.admin.views import views

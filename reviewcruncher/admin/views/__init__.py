from flask import Blueprint

myadmin = Blueprint('myadmin', __name__)

from reviewcruncher.admin.views import registration
from reviewcruncher.admin.views import upload_product

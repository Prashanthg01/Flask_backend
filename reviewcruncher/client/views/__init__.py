from flask import Blueprint

client = Blueprint('client', __name__)

from reviewcruncher.client.views import landing_pages
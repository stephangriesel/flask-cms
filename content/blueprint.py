from flask import Blueprint
from flask import render_template

content = Blueprint('content', __name__, template_folder='templates')

# localhost:5050/content/mediapack
@content.route('/mediapack')
def content_list_mediapack():
    return render_template('content/mediapack.html')

# localhost:5050/content/forms
@content.route('/forms')
def content_list_forms():
    return render_template('content/forms.html')

# localhost:5050/content/projectvideos
@content.route('/projectvideos')
def content_list_projectvideos():
    return render_template('content/projectvideos.html')

# localhost:5050/content/annualreports
@content.route('/annualreports')
def content_list_annualreports():
    return render_template('content/annualreports.html')

# localhost:5050/content/articlelinks
@content.route('/articlelinks')
def content_list_articlelinks():
    return render_template('content/articlelinks.html')

static = Blueprint('static', __name__, template_folder='templates')

# localhost:5050/static/donations
@static.route('/donations')
def static_list_donations():
    return render_template('static/donations.html')

# localhost:5050/static/contact
@static.route('/contact')
def static_list_contact():
    return render_template('static/contact.html')
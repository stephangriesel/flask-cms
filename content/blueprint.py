from flask import Blueprint
from flask import render_template

content = Blueprint('content', __name__, template_folder='templates')

# localhost:5050/mediapack
@content.route('/mediapack')
def content_list_mediapack():
    return render_template('content/mediapack.html')

# localhost:5050/forms
@content.route('/forms')
def content_list_forms():
    return render_template('content/forms.html')

# localhost:5050/projectvideos
@content.route('/projectvideos')
def content_list_projectvideos():
    return render_template('content/projectvideos.html')

# localhost:5050/annualreports
@content.route('/annualreports')
def content_list_annualreports():
    return render_template('content/annualreports.html')

# localhost:5050/articlelinks
@content.route('/articlelinks')
def content_list_articlelinks():
    return render_template('content/articlelinks.html')
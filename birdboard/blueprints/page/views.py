from flask import Blueprint, render_template
import requests 

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    return render_template('page/home.html')


@page.route('/get_api_info')
def get_api_info():
	data = requests.get('https://api.openaq.org/v1/cities')
	print(data.keys())
	return False

@page.route('/healthy')
def healthy():
	return ''


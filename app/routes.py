import os
from flask import send_from_directory
from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Rob'}
	return render_template('index.html', title='Home', user=user)

@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/camera')
def camera():
	user = {'username': 'Rob'}
	return render_template('camera.html', title='Camera-unit', user=user)

@app.route('/rpi')
def rpi():
	user = {'username': 'Rob'}
	return render_template('rpi.html', title='Basisunit', user=user)
	

@app.route('/c4ylo')
def c4ylo():
	user = {'username': 'Rob'}
	return render_template('c4ylo.html', title='C4YLO server', user=user)

@app.route('/smartphone')
def smartphone():
	user = {'username': 'Rob'}
	return render_template('smartphone.html', title='Smartphone', user=user)

@app.route('/kids')
def kids():
	user = {'username': 'Rob'}
	return render_template('kids.html', title='Voor de kids', user=user)

@app.route('/prices')
def prices():
	user = {'username': 'Rob'}
	return render_template('prices.html', title='Prijzen', user=user)

@app.route('/contact')
def contact():
	user = {'username': 'Rob'}
	return render_template('contact.html', title='Contact', user=user)

@app.route('/login')
def login():
	form = LoginForm
	return render_template('login.html', title='Sign In', form=form)

@app.route('/voorbeeld')
def voorbeeld():
	user = {'username': 'Rob'}
	return render_template('voorbeeld.html', title='Voorbeeld', user=user)
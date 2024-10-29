from flask import Blueprint, render_template, url_for, request

authBp = Blueprint('authentication', __name__)

@authBp.route('/')
def landingPage():
    return render_template('/landing_page.html')

@authBp.route('/signup')
def signup():
    return render_template('signup.html')

@authBp.route('/login')
def login():
    return render_template('login.html')
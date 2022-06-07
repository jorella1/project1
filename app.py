from flask import Flask, render_template, request, url_for, redirect, abort
from flask_login import LoginManager, current_user, login_required
from flask_bootstrap import Bootstrap
from models.user_dto import User
from nav import nav
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from service.login_service import login_success, verify_login


app = Flask(__name__)
Bootstrap(app)
nav.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()

nav.register_element('frontend_top', Navbar(
    View('Project 1', '.index'),
    View('Home', '.index'),
    View('Login', '.login_page'),
    ))


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/login')
def login_page():
    return render_template("login.html")

@app.route('/login',methods=["POST"])
def login_check():
    return verify_login(request.form)

@app.route('/profile')
@login_required
def load_profile():
    return render_template("profile.html",name=current_user.name)

if __name__== "__main__":
    app.run()
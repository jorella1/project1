from flask import Flask, render_template, request, url_for, redirect, abort
from flask_bootstrap import Bootstrap
from nav import nav
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from service.login_service import login_success, verify_login


app = Flask(__name__)
Bootstrap(app)
nav.init_app(app)

nav.register_element('frontend_top', Navbar(
    View('Project 1', '.index'),
    View('Home', '.index'),
    View('Login', '.login_page'),
    ))



@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route('/login/verify',methods=["GET","POST"])
def login_check():
    return verify_login(request.form)

@app.route('/home/<str:type>',methods=["GET","POST"])
def login_check(type):
    return login_success(type)

if __name__== "__main__":
    app.run()
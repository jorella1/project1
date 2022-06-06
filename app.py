from flask import Flask, render_template, request, url_for, redirect, abort
from flask_bootstrap import Bootstrap
from nav import nav
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator


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
    pass

if __name__== "__main__":
    app.run()
from flask import Flask, render_template, request, url_for, redirect
from flask_login import LoginManager, current_user, login_required, logout_user
from flask_bootstrap import Bootstrap
from nav import nav
from flask_nav.elements import Navbar, View
from repo.login_dao import select_user_byid
from service.login_service import verify_login
from service.request_service import reimbursement_request
from flask import Response as make_response


app = Flask(__name__)
Bootstrap(app)
nav.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'app.login_page'
login_manager.init_app(app)
app.secret_key = '123456789'

@login_manager.user_loader
def load_user(user_id):
    return select_user_byid(user_id)

nav.register_element('frontend_top', Navbar(
    View('Project 1', '.index'),
    View('Home', '.login_page'),
    View('Login', '.login_page'),
    View('Logout', '.logout'),
    ))

#Landing Page
@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

#Login
@app.route('/login', methods = ["GET","POST"])
def login_page():
    if request.method == "GET":
        if current_user.is_active:
            return redirect(url_for('.load_profile',type = current_user.account_type))
        return render_template("login.html")
    else:
        return verify_login(request.form) 

#Home Page after Login
@app.route('/profile/<type>')
@login_required
def load_profile(type):
    type = current_user.account_type
    if type == "Manager":
       return render_template("profile.html",name=current_user.username)       
    elif type == "Employee":
        return render_template("profile.html",name=current_user.username)

#Request Submission    
@app.route('/request/submission', methods = ["POST"])
@login_required
def submit_request():
    return reimbursement_request(request.form)

#Logout Button
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login_page'))
    
if __name__== "__main__":
    app.run(debug=True)


from flask import (Blueprint, Flask, current_app, redirect, render_template,
                   request, url_for)
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, current_user, login_required, logout_user
from flask_nav.elements import Navbar, View

from . import main
from .nav import nav
from .repo.login_dao import select_user_byid
from .service.login_service import verify_login
from .service.request_service import (alter_request, cancel_requests,
                                      employee_profile, manager_profile,
                                      reimbursement_request)

main = Blueprint('main', __name__, template_folder='templates')

#Landing Page
@main.route('/', methods=["GET"])
def index():
    return render_template('index.html')

#Login
@main.route('/login', methods = ["GET","POST"])
def login_page():
    if request.method == "GET":
        if current_user.is_active:   
            return redirect(url_for('.load_profile',type = current_user.account_type))
        return render_template("login.html")
    else:
        current_app.logger.info('%s is attempting to login', request.form.get("user_name"))
        return verify_login(request.form) 

#Home Page after Login
@main.route('/profile/<type>')
@login_required
def load_profile(type):
    if current_user.is_active == False:
        return redirect(url_for('.login_page'))
    type = current_user.account_type
    
    if type == "Manager":
        current_app.logger.info('%s logged in successfully as a Manager', current_user.username)
        return manager_profile()
    
    elif type == "Employee":
        current_app.logger.info('%s logged in successfully as an Employee', current_user.username)
        return employee_profile()


#Request Submission    
@main.route('/request/submission', methods = ["POST"])
@login_required
def submit_request():
    if current_user.is_active() == False:
        return redirect(url_for('.login_page'))
    current_app.logger.info('%s is submitting a request', current_user.username)
    return reimbursement_request(request.form)

#Alter request
@main.route('/request/alter',methods =["POST"])
@login_required
def handle_request():
    if current_user.is_active() == False:
        return redirect(url_for('.login_page'))
    current_app.logger.info('%s is updating a request', current_user.username)
    return alter_request(request.form)

@main.route('/request/cancel',methods =["POST"])
@login_required
def cancel_request():    
    if current_user.is_active() == False:
        return redirect(url_for('.login_page'))
    current_app.logger.info('%s is canceling their request', current_user.username)
    return cancel_requests(request.form)

#Logout Button
@main.route('/logout')
@login_required
def logout():
    current_app.logger.info('%s is logging out', current_user.username)
    logout_user()
    return redirect(url_for('main.login_page'))
    
#if __name__== "__main__":
#    app.run(debug=True)

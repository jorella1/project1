from logging import FileHandler, StreamHandler
from logging.config import dictConfig
from flask import Flask, render_template, request, url_for, redirect
from flask_login import LoginManager, current_user, login_required, logout_user
from flask_bootstrap import Bootstrap
from nav import nav
from flask_nav.elements import Navbar, View
from repo.login_dao import select_user_byid
from service.login_service import verify_login
from service.request_service import reimbursement_request, manager_profile, employee_profile, alter_request, cancel_requests

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    },
    'file': {'class': 'logging.FileHandler',
        'filename': 'status.log'
    }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi', 'file']
    }
}) 

app = Flask(__name__)
Bootstrap(app)
nav.init_app(app)

login_manager = LoginManager()
login_manager.login_view = '.login_page'
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
        app.logger.info('%s is attempting to login', request.form.get("user_name"))
        return verify_login(request.form) 

#Home Page after Login
@app.route('/profile/<type>')
@login_required
def load_profile(type):
    if current_user.is_active == False:
        return redirect(url_for('.login_page'))
    type = current_user.account_type
    
    if type == "Manager":
        app.logger.info('%s logged in successfully as a Manager', current_user.username)
        return manager_profile()
    
    elif type == "Employee":
        app.logger.info('%s logged in successfully as an Employee', current_user.username)
        return employee_profile()


#Request Submission    
@app.route('/request/submission', methods = ["POST"])
@login_required
def submit_request():
    if current_user.is_active() == False:
        return redirect(url_for('.login_page'))
    app.logger.info('%s is submitting a request', current_user.username)
    return reimbursement_request(request.form)

@app.route('/request/submit',methods =["POST"])
@login_required
def handle_request():
    if current_user.is_active() == False:
        return redirect(url_for('.login_page'))
    app.logger.info('%s is updating a request', current_user.username)
    return alter_request(request.form)

@app.route('/request/cancel',methods =["POST"])
@login_required
def cancel_request():    
    if current_user.is_active() == False:
        return redirect(url_for('.login_page'))
    app.logger.info('%s is canceling their request', current_user.username)
    return cancel_requests(request.form)

#Logout Button
@app.route('/logout')
@login_required
def logout():
    app.logger.info('%s is logging out', current_user.username)
    logout_user()
    return redirect(url_for('login_page'))
    
if __name__== "__main__":
    app.run(debug=True)

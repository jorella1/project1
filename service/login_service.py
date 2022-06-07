from flask import render_template, url_for
from flask_login import LoginManager
from models.user_dto import User
from repo.login_dao import select_user

@LoginManager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()

def verify_login(form):
    login_dto = select_user(form.get("username"),form.get("password"))
    if login_dto.id.is_authenticated() == False:
        return render_template("login.html")
    else:
        return login_success(login_dto.account_type)

def login_success(position):
    if position == "Manager":
        return render_template("managerHome.html")
    elif position == "Employee":
        return render_template("employeeHome.html")
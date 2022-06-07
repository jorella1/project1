from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user
from models.user_dto import User
from repo.login_dao import select_user



def verify_login(form):
    login_dto = select_user(form.get("user_name"),form.get("user_pass"))
    if login_dto is None:
        flash('Please check your login details and try again.')
        return redirect(url_for('login_check'))
    
    if login_dto.account_type == "Manager":
        login_user(login_dto)
        #User.is_authenticated()
        return redirect(url_for(".load_profile",type = login_dto.account_type))
    elif login_dto.account_type == "Employee":
        print(login_dto)
        login_user(login_dto)
        #User.is_authenticated()
        return redirect(url_for(".load_profile",type = current_user.account_type))

def render_profile_page(type):
    return 
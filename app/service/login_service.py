from app.models.user_dto import User
from app.repo.login_dao import select_user
from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user


def verify_login(form):
    login_dto = select_user(form.get("user_name"),form.get("user_pass"))
    if login_dto is None:
        flash('Please check your login details and try again.')
        return redirect(url_for('login_page'))
    
    login_user(login_dto)

    return redirect(url_for(".load_profile",type = current_user.account_type))
    

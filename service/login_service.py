from flask import flash, redirect, render_template, url_for
from flask_login import login_user
from repo.login_dao import select_user



def verify_login(form):
    login_dto = select_user(form.get("username"),form.get("password"))

    if login_dto is None:
        flash('Please check your login details and try again.')
        return redirect(url_for('login.html'))
    
    login_user(login_dto)
    return redirect(url_for('app.profile'))

def login_success(position):
    if position == "Manager":
        return render_template("managerHome.html")
    elif position == "Employee":
        return render_template("employeeHome.html")
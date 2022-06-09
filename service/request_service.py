from cProfile import label
from flask import flash, redirect, url_for, render_template
from flask_login import current_user
from repo.request_dao import alter_request_status, cancel_user_request, get_request, new_reimbursement_request, get_request_table, get_user_requests



def reimbursement_request(form):
    new_reimbursement_request(current_user,form.get("amount"),form.get("description"))
    flash('reimbursement request successfully submitted.')
    return redirect(url_for(".load_profile",type = current_user.account_type))

def alter_request(form):
    request_dto = get_request(form.get("request_id"))
    print(request_dto.username)
    if int(current_user.id) == request_dto.user_id:
        flash("Users cannot modify their own requests")
        return redirect(url_for(".load_profile",type = current_user.account_type))
    elif request_dto.id is None:
        flash("Invalid Input")
        return redirect(url_for(".load_profile",type = current_user.account_type))
    alter_request_status(request_dto.id, form.get("update_status"))
    return redirect(url_for(".load_profile",type = current_user.account_type))

def manager_profile():
    all_requests = get_request_table()
    emp_requests = get_user_requests(current_user.id)
    return render_template("profile.html",name=current_user.username,curr_requests= emp_requests ,all_requests= all_requests) 

def employee_profile():
    emp_requests = get_user_requests(current_user.id)
    return render_template("profile.html",name=current_user.username, curr_requests= emp_requests)

def cancel_requests(form):
    request_dto = get_request(form.get("cancel_id"))
    if request_dto == None or int(current_user.id) != request_dto.user_id:
        flash("You can only cancel your own requests")
        return redirect(url_for(".load_profile",type = current_user.account_type))
    cancel_user_request(form.get("cancel_id"))
    flash(f"You have deleted Request {request_dto.id}")
    return redirect(url_for(".load_profile",type = current_user.account_type))
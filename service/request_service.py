from flask import flash, redirect, url_for
from flask_login import current_user
from repo.request_dao import new_reimbursement_request
import pandas as pd


def reimbursement_request(form):
    new_reimbursement_request(current_user,form.get("amount"),form.get("description"))
    flash('reimbursement request successfully submitted.')
    return redirect(url_for(".load_profile",type = current_user.account_type))
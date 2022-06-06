from flask_login import is_authenticated
from repo.login_dao import select_user

def login_success():
    login_dto = select_user()

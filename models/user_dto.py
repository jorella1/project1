from csv import unregister_dialect
from ssl import _PasswordType


class User:
    def __init__(self,user_id,username,password,account_type):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.account_type = account_type


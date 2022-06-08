class User:
    def __init__(self,id,username,password,account_type):
        self.id = id
        self.username = username
        self.password = password
        self.account_type = account_type
    
    def _repr__(self):
        return print(f"Current User: {self.id}")
        
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)
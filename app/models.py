from . import db
class User(db.Model):
    user_id = db.Column(db.Integer() ,primary_key = True)
    FirstName = db.Column(db.String(255))
    LastName = db.Column(db.String(255))
    D_O_B = db.Column(db.String(255))
    email = db.Column(db.String(255))
    Phone = db.Column(db.String(255))
    Password = db.Column(db.String(255))
    
    __tablename__ = "user"
    def __init__(self,FirstName,LastName,D_O_B,Email,Phone,Password):
        self.FirstName = FirstName
        self.LastName = LastName
        self.D_O_B = D_O_B
        self.email = Email
        self.Phone = Phone
        self.Password = Password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.user_id)  # python 2 support
        except NameError:
            return int(self.user_id)  # python 3 support

        
        
        
        

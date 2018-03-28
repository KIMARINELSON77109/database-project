from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import Required


class LoginForm(Form):
    email = StringField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    
class SignUpForm(Form):
    firstname = StringField('FirstName',validators=[Required()])
    lastname = StringField('LastName',validators=[Required()])
    email = StringField('Email',validators=[Required()])
    phone = StringField('Phone',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    D_O_B = SelectField('D_O_B',validators=[Required()])

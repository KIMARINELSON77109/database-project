from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SelectField, FileField, SubmitField
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
    D_O_B = StringField('D_O_B',validators=[Required()])

class RecipeForm(Form):
    uploadedfile = FileField("Upload A Picture")
    name = StringField("Recipe Name",validators=[Required()])
    serving = StringField("Serving",validators=[Required()])
    preptime = StringField("Preparation Time",validators=[Required()])
    cooktime = StringField("Cook Time",validators=[Required()])
    instruction = StringField("instruction",validators=[Required()])
    submit = SubmitField("Submit")
    
class GenPlanForm(Form):
    calorie = StringField("Enter a calorie count")
    submit = SubmitField("Generate Plan")
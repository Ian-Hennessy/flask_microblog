from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# a new class which defines a form for logigng into the web application 
class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = StringField('Password:', validators=[DataRequired()])
    remember_me = BooleanField('Remember me:')
    submit = SubmitField('Sign In')
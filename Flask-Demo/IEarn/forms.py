from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,IntegerField,widgets
from wtforms.validators import InputRequired,Length,Email,EqualTo


############ forms

class Loginform(FlaskForm):
    email = StringField('Email Id',validators=[InputRequired(), Email(message="Invalid Email")])
    password = PasswordField('Password',validators=[InputRequired(),Length(min=8,max=16)])
    remember = BooleanField('Remember me')


class Registrationform(FlaskForm):
    user_name = StringField('Name', validators=[InputRequired()])
    user_email = StringField('Email Id',validators=[InputRequired(), Email(message="Invalid Email ")])
    user_phoneno = IntegerField('Phone Number' ,widget = widgets.Input(input_type="number"))
    user_password = PasswordField('Password',[InputRequired(), Length(min=8),
               EqualTo('confirm', message='Passwords & Confirm Password must match!')])
    confirm=PasswordField('Confirm Password')

from myproject.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email= StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

class RegistrationForm(FlaskForm):
    email= StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirm', message = "Password must match.")])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('submit')

    def check_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("Your email has already been registered.")
    
    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError("This username is taken.")
    
    def validate_username(self, field): 
        # When form.validate_on_submit() is called in the route, 
        # Flask-WTF goes through all the validation methods defined in the form. This includes:
        # Built-in validators such as DataRequired(), Email(), etc.
        # Custom validation methods like validate_username
        username = field.data
        lower_letter = any(c.islower() for c in username)
        upper_letter = any(c.isupper() for c in username)
        num_end = username[-1].isdigit() if username else False

        # Check if all conditions are met
        if not lower_letter:
            raise ValidationError("You must include at least one lowercase letter.")
        if not upper_letter:
            raise ValidationError("You must include at least one uppercase letter.")
        if not num_end:
            raise ValidationError("Your username must end with a number.")
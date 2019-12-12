from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[
                               DataRequired(),
                               Length(min=2, max=20)
                           ])

    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ])

    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                                 Regexp(regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
                                        message='''Password must be minimum 8 characters,
                                        at least 1 letter and 1 number''')
                             ])

    confirm_password = PasswordField('Confirm Password',
                                     validators=[
                                         DataRequired(),
                                         EqualTo('password')
                                     ])

    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('username already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email already taken.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ])

    password = PasswordField('Password',
                             validators=[
                                 DataRequired()
                             ])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')

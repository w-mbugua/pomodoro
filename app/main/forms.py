from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TimeField
from wtforms import validators
from wtforms.validators import DataRequired, Email, EqualTo,Required, ValidationError
from ..models import User

class PomodoroForm(FlaskForm):
    intervals = IntegerField('Enter the number of pomodoros', validators=[DataRequired()])
    work = IntegerField('How long do you want to work for? (Enter Minutes)', validators=[DataRequired()])
    rest = IntegerField('How long do you want to rest for? (Enter Minutes)', validators=[DataRequired()])
    submit = SubmitField('Create')
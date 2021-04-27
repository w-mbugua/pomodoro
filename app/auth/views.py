from flask import render_template
from .forms import RegistrationForm
from . import auth



@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('auth/register.html', title = 'Register', form = form)


@auth.route('/login')
def login():
    pass


@auth.route('/logout')
def logout():
    pass
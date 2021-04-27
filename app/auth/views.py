from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user
from .forms import LoginForm
from . import auth


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()


        

    title = "watchlist login"
    return render_template('auth/login.html',login_form = login_form,title=title)

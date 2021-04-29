from flask import render_template, url_for, redirect
from flask.helpers import flash
from . import main
from flask_login import login_required, current_user
from .forms import PomodoroForm
from ..models import User, Timer
from .. import db
import time

@main.route('/')
def index():
   
    pomodoros = Timer.query.all()
    title = 'Home Page'
    return render_template('index.html', title = title, pomodoros = pomodoros)


@main.route('/form/pomodoro', methods = ['GET', 'POST'])
@login_required
def create_timer():
    form = PomodoroForm()
    if form.validate_on_submit():
        pomodoro = Timer(timer_length = form.work.data, break_length = form.rest.data, user = current_user)
        db.session.add(pomodoro)
        db.session.commit()
        flash('Your pomodoro has been created!')
        return redirect(url_for('main.timer', id = pomodoro.id))
    return render_template('create_timer.html', title = 'Pomodoro Clock', form = form) 

@main.route('/pomodoro/<int:id>')
def timer(id):
    pomodoro = Timer.query.get_or_404(id)
    return render_template('pomodoro.html', title = 'My Pomodoro', pomodoro = pomodoro)

@main.route('/playground')
def play():
    return render_template('main.html')


    


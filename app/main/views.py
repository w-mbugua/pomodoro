from flask import render_template, url_for, redirect
from flask.helpers import flash
from . import main
from flask_login import login_required
from .forms import PomodoroForm
from ..models import User, Timer

@main.route('/')
def index():
    title = 'Home Page'
    return render_template('index.html', title = title)

@main.route('/pomodoro')
def timer(timer_id):
    pomodoro = Timer.query.filter_by(id = timer_id).first_or_404()

    return render_template('pomodoro.html', title = 'My Pomodoro')


@main.route('/form/pomodoro', methods = ['GET', 'POST'])
def create_timer():
    form = PomodoroForm()
    if form.validate_on_submit():
        flash('Your pomodor has been created!')
        return redirect(url_for('main.pomodoro'))
    return render_template('timer.html', title = 'Pomodoro Clock', form = form) 

@main.route('/user/<name>')
def profile(name):
    pass


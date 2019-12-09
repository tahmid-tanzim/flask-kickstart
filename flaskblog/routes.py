from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [{
    'author': 'Tahmid Tanzim Lupin',
    'date_posted': '25th March, 2019',
    'title': 'Lorem Ipsum',
    'content': 'Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum'
}, {
    'author': 'Tahmid Tanzim Lupin',
    'date_posted': '25th March, 2019',
    'title': 'Lorem Ipsum',
    'content': 'Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum'
}]


@app.route('/')
@app.route('/home')
def dashboard():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about_us():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('dashboard'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login success', 'success')
        return redirect(url_for('dashboard'))
    return render_template('login.html', title='Login', form=form)

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e3f6db2fe4ec99f04db9b1c1ab0cc55f'

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
def about():
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


if __name__ == "__main__":
    app.run(debug=True)

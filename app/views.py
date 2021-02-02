from flask import Flask, render_template, url_for, flash, redirect
from .forms import RegistrationForm, LoginForm
from app import app

app.config['SECRET_KEY'] = 'd9ee7cf4cfc30af058b1dd9c649c0b82'

#this would be called from the database
posts = [
    {
        'author': 'Frannie Ziesemer',
        'title': 'Blog Post 1',
        'content': 'First post content....',
        'date_posted': 'February 1, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2 ',
        'content': 'Second Post content....',
        'date_posted': 'February 2, 2021'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else: 
            flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
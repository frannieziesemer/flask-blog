from flask import Flask, render_template, url_for, flash, redirect
from app import app
from forms import RegistrationForm, LoginForm

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
def index():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user = {'Username': 'Ian'}
    posts = [
        {
            'author': {'Username': 'Ian'},
            'body': 'first post'
        },
        {
            'author': {'Username': 'John'},
            'body': 'second post'
        }
    ]
    return render_template('index.html', title="HOME", user=user, posts=posts)
@app.route('/login', methods=['get','post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():  
        flash('Login requested for user {}, remember_me= {}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')

    return render_template('login.html', title="Sign In", form=form)
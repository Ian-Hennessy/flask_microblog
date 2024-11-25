from flask import render_template
from app import app
from forms import LoginForm

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

def login():
    form = LoginForm()
    return render_template('login.html', title="Sign In", form=form)
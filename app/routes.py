from flask import render_template

from app import app

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
    print(posts)
    return render_template('index.html', title="HOME", user=user, posts=posts)
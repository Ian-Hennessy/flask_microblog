from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'Username': 'Ian'}
    posts = [
        {
            'author': {'Username': 'Ian'},
  
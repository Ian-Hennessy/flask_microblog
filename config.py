import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Establish Secret Key for CSRF attack robustness
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Theresasnakeinmyboot17!'

    # Establish a database reference for storing, accessing, 
    # etc data on the application
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
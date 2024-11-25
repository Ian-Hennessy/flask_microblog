import os

class Config:
    SECRET_KEY = os.environ.gt('SECRET_KEY') or 'Theresasnakeinmyboot17!'
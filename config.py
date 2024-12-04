import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'hmmmmmmmmmmmmmmmmmmmmmmmmm'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')  # Use MySQL URI for MySQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
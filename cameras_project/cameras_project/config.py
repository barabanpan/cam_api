import os
import datetime
from dotenv import dotenv_values

project_root = os.getcwd()
env = dotenv_values(os.path.join(project_root, ".env"))


class Config(object):
    DEBUG = env['DEBUG']
    SECRET_KEY = env['SECRET_KEY']
    SECURE_SSL_REDIRECT = env['SECURE_SSL_REDIRECT']

    # postgresql configuration
    DB_NAME = env['DB_NAME']
    DB_USER = env['DB_USER']
    DB_PASSWORD = env['DB_PASSWORD']
    DB_HOST = env['DB_HOST']
    DB_PORT = env['DB_PORT']


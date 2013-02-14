#!/bin/env python

from base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += ('django.contrib.admin',)

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

try:
    _password = os.environ['MYSQL_PASS']
except KeyError:
    _password = getpass.getpass('Mysql password >')
    os.environ['MYSQL_PASS'] = _password

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'agagd',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': _password,                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

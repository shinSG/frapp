#!/usr/bin/python
# coding=utf-8

import os

BASE_DIR = os.path.dirname(__name__)

DB_CONNECTION = 'MySQL'

DB_HOST = 'localhost'
DB_PORT = 27017
DB_USERNAME = ''
DB_PASSWD = ''


INSTALL_APPS = [
    'apps.login'
]


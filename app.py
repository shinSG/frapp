#!/usr/bin/python
# coding=utf-8

from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine
import config


web_site = Flask(__name__)
api = Api(web_site)
db = MongoEngine(web_site)

subapps = config.INSTALL_APPS

for app in subapps:
    api.add_resource(TApi, '/<string:id>')


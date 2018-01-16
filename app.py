#!/usr/bin/python
# coding=utf-8

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello():
    return 'f**k'


class TApi(Resource):
    def get(self, id):
        return {'aaa': id}

api.add_resource(TApi, '/<string:id>')


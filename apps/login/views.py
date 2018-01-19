#!/usr/bin/python
# coding=utf-8

from flask import request
from flask_restful import Resource


class Login(Resource):
    def post(self):
        form = request.form


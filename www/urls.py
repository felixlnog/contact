# -*- coding: utf-8 -*-

from transwarp.web import get, view, seeother
from models import Contact


@view('/auth.html')
@get('/auth')
def login():
    return dict()

@view('/contactlist.html')
@get('/')
def list():
    return dict()
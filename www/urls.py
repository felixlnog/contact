# -*- coding: utf-8 -*-

from transwarp.web import get, view, seeother,post,ctx,notfound
from models import Contact
from apis import api,APIError,APIValueError,APIResourceNotFoundError

@view('/auth.html')
@get('/auth')
def login():
    return dict()

@view('/index.html')
@get('/')
def list():
    return dict()

@view('contactlist.html')
# @api
@get('/contactlist/:id')
def contactlist(id):
	contact = Contact.find_first('where id=?',id)
	if contact is None:
		raise notfound()
	contactlist = Contact.find_by('where groupid=?',contact.groupid)
	if contactlist:
		return dict(contactlist=contactlist,group=contact.groupid)
	else:
		raise APIResourceNotFoundError(contact.groupid,'failed')

@api
@post('/api/auth')
def auth():
	i = ctx.request.input(phoneid='')
	phoneid = i.phoneid.strip()
	contact = Contact.find_first('where tel=?',phoneid)
	contact1 = Contact.find_first('where work_tel=?',phoneid)
	if contact:
		return dict(contact)
	elif contact1:
		return dict(contact1)
	else :
		raise APIResourceNotFoundError(phoneid,'failed')




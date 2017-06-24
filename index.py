# -*- coding: utf-8 -*-

import xmlrpclib

url_object = 'http://chocotech.trustcode.com.br/xmlrpc/object'
url_auth = 'http://chocotech.trustcode.com.br/xmlrpc/common'
db = 'chocotech'
username = 'demo'
password = 'demo'

# OpenERP Common login Service proxy object 
sock_common = xmlrpclib.ServerProxy(url_auth)
uid = sock_common.authenticate(db, username, password, {})

if uid:
	print "\nLogin realizado com secesso. \n"
else:
	print "\nVerifique as credenciais de acesso."
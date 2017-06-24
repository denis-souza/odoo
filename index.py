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

sock = xmlrpclib.ServerProxy(url_object)

# Insert a new customer
id_new_customer = sock.execute_kw(db, uid, password, 'res.partner', 'create', [{
  'name': "Cliente 82",
  'email': "cliente82@teste.com",
  'phone': "(48) 99884-9093",
  'zip': "88037-908"
}])

if id_new_customer:
	print 'Cliente cadastrado com sucesso! \n'
	print 'ID: ' + str(id_new_customer) + '\n'
else:
	print 'Não foi possivel salvar o registro do cliente! \n'
# -*- coding: utf-8 -*-
import xmlrpclib

#odooActivities.py
class odooActivities(object):
	
  def __init__(self):
    self.url_object = 'http://chocotech.trustcode.com.br/xmlrpc/object'
    self.url_auth = 'http://chocotech.trustcode.com.br/xmlrpc/common'
    self.db = 'chocotech'
    self.username = 'demo'
    self.password = 'demo'
    self.sock = xmlrpclib.ServerProxy(self.url_object)
    self.uid = 0

  def authenticate(self):
		try:
			sock_common = xmlrpclib.ServerProxy(self.url_auth)
			uid = sock_common.authenticate(self.db, self.username, self.password, {})

			if uid:
				self.uid = uid

				print "\nLogin realizado com secesso. \n"
			else:
				print "\nVerifique as credenciais de acesso."
		except:
			print "\nOcorreu um erro, contate com o administrador.\n"

  def insert(self, name, email, phone, zip_code):
    try:
      # Insert a new customer.
      id_new_customer = self.sock.execute_kw(self.db, self.uid, self.password, 'res.partner', 'create', [{
        'name': name,
        'email': email,
        'phone': phone,
        'zip': zip_code
      }])
  
      if id_new_customer:
        print '\nCliente cadastrado com sucesso! \n'
        print 'ID: ' + str(id_new_customer) + '\n'
      else:
        print 'Não foi possivel salvar o registro do cliente! \n'
    except:
      print "\nOcorreu um erro, contate o administrador.\n"
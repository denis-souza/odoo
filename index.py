# -*- coding: utf-8 -*-
import xmlrpclib

#odooActivities.py
class odooActivities():

  def __init__(self):
    self.url_object = 'http://chocotech.trustcode.com.br/xmlrpc/object'
    self.url_auth = 'http://chocotech.trustcode.com.br/xmlrpc/common'
    self.db = 'chocotech'
    self.username = 'demo'
    self.password = 'demo'
    self.sock = xmlrpclib.ServerProxy(self.url_object)
    self.uid = 0
    self.customer_id = 0

  def authenticate(self):
    try:
      sock_common = xmlrpclib.ServerProxy(self.url_auth)
      uid = sock_common.authenticate(self.db, self.username, self.password, {})

      if uid:
        self.uid = uid

        print '\nLogin realizado com secesso. \n'
      else:
        print '\nVerifique as credenciais de acesso.'
    except:
      print '\nOcorreu um erro, contate com o administrador.\n'

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
        self.customer_id = id_new_customer

        print '\nCliente cadastrado com sucesso! \n'
        print 'ID: ' + str(id_new_customer) + '\n'
      else:
        print '\nNão foi possivel salvar o registro do cliente! \n'
    except:
      print '\nOcorreu um erro, contate o administrador.\n'

  def update(self, rg_fisica):
    try:
      #Update record.
      update = self.sock.execute_kw(self.db, self.uid, self.password, 'res.partner', 'write', [
        [self.customer_id], {'rg_fisica': rg_fisica}
      ])
  
      if update:
        print '\nRG atualizado com sucesso.\n'
      else:
        print '\nNão foi possível atualizar o registro.\n'
    except:
      print '\nOcorreu um erro, contate o administrador.\n'

  def count(self):
    try:
      count = self.sock.execute_kw(self.db, self.uid, self.password, 'res.partner', 'search_count', [
      	[['customer', '=', True]]])

      print '\nAtualmente existem ' + str(count) + ' clientes na base.\n'
    except:
      print '\nOcorreu um erro, contate o administrador.\n'

  def list_customers_ordering_name(self):
    try:
      # List 10 customers oredering by name
      items = self.sock.execute_kw(self.db, self.uid, self.password,
        'res.partner', 'search_read',
        [[['customer', '=', True]]],
        {'fields': ['name', 'state_id'], 'order': 'name ASC', 'limit': 10}
      )

      for item in items:
        print item  
    
    except:
      print '\nOcorreu um erro, contate o administrador.\n'

  def list_greatest_sale_made(self):
    try:
      # List greatest sale made
      items = self.sock.execute_kw(self.db, self.uid, self.password,
        'sale.order', 'search_read',
        [[['state', '=', 'sale']]],
        {'fields': ['amount_total', 'partner_invoice_id'], 'order': 'amount_total desc', 'limit': 1})

      for item in items:
        print item
    except:
      print '\nOcorreu um erro, contate o administrador.\n'

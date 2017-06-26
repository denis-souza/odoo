Integration Odoo
=======

This is a python script to run some calls using the odoo api.

Features supported:

* Authenticate demo user.
* Insert a new customer.
* Update RG Fisica customer.
* Present the number of registered customers at the base.
* List the top ten customers in alphabetical order.
* List the largest sale made.
* List the items of the larger sale made.
* Present the percentage in sales.

How does it work? See below:

Authenticated
------------------------------

To make any call via API you must be authenticated. At the terminal run the following command
```python
python index.py
>>> from index import odooActivities
>>> obj = odooActivities()
>>> obj.authenticate()
```
After being authenticated you can use the activities available in the script with the Odoo API.

Insert new customer
------------------------------

```python
>>> obj.insert('name', 'email', 'phone', 'zip_code')
```
Update RG customer
------------------------------

```python
>>> obj.update('number_rg_fisica')
```
Count number of customers
------------------------------

```python
>>> obj.count()
```
List customers ordering name
------------------------------

```python
>>> obj.list_customers_ordering_name()
```
List greatest sale made
------------------------------

```python
>>> obj.list_greatest_sale_made()
```

List order line greatest sale made
------------------------------
```python
>>> obj.list_order_line_greatest_sale_made()
```
Show Percentage Sales
------------------------------
```python
>>> obj.show_percentage_sales()
```

from flask import Blueprint, render_template

cliente_route = Blueprint('home', __name__)
"""
Rota de clientes

  - /clientes/ (GET) - listar os clientes
  - /clientes/ (POST) - inserir o cliente no servidor
  - /clientes/new - (GET) - renderizar o formulario para criar um cliente
  - /clientes/<id> (GET) - obter os clientes
  - /clientes/<id>/edit - (GET) renderizar um formulario para editar um cliente
  - /clientes/<id>/update - (PUT) atuaizar os dados do clientes
  - /clientes/<id>/delete - (DELETE) delete o cliente


"""

@cliente_route.route('/')
def lista_clientes():
  pass

#inserindo cliente
@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
  pass

#puxando o formulario para cadastrar cliente
@cliente_route.route('/new')
def new_cliente():
  pass

#puxando o formulario para detalhar o cliente
@cliente_route.route('/<int: cliente_id>')
def detalhe_cliente(cliente_id):
  pass

#formulario para editar um cliente
@cliente_route.route('/<int: cliente_id>/edit')
def detalhe_cliente(cliente_id):
  pass
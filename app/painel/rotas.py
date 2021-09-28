from sqlalchemy import desc, func

from flask import render_template, Blueprint, flash, redirect, url_for, current_app

from flask.views import View

from ..modelos import db, Empresa, Pedido, Produto, Unidade, PontoDeVenda, Usuario, Entrega


from ..biblioteca.consultar_pedidos import lista_pedidos
from ..biblioteca.consultar_entregas import lista_entregas

#from flask_socketio import SocketIO
#from .. import socketio


painel_blueprint = Blueprint(
    'painel',
    __name__,
    template_folder='../templates/painel',
    url_prefix="/painel"
)





"""
@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
"""




@painel_blueprint.route('/')
def painel():

    pedidos = lista_pedidos()

    return render_template(
        'index.html',
        pedidos=pedidos
    )

@painel_blueprint.route('/pedidos')
def pedidos():

    pedidos = lista_pedidos()

    return render_template(
        'pedidos.html',
        pedidos=pedidos
    )









class ExibirLista(View):

    def selecionar_nome_template(self):
        
        return NotImplementedError()

    def render_template(self, contexto):
        
        return render_template(self.selecionar_nome_template(), **contexto)

    def dispatch_request(self):
        
        contexto = {'objects': self.get_objects()}

        return self.render_template(contexto)


class ExibirUsuarios(ExibirLista):

    def selecionar_nome_template(self):
        return 'usuarios.html'

    def get_objects(self):
        return Usuario.query.all()


class ExibirEmpresas(ExibirLista):

    def selecionar_nome_template(self):
        return 'empresas.html'

    def get_objects(self):
        return Empresa.query.all()


class ExibirPedidos(ExibirLista):

    def selecionar_nome_template(self):
        return 'pedidos.html'

    def get_objects(self):
        return Pedido.query.all()


class ExibirProdutos(ExibirLista):

    def selecionar_nome_template(self):
        return 'produtos.html'

    def get_objects(self):
        return Produto.query.all()


class ExibirUnidades(ExibirLista):

    def selecionar_nome_template(self):
        return 'unidades.html'

    def get_objects(self):
        return Unidade.query.all()





# ROTAS GERENTE REGIONAL




# ROTAS DO GERENTE

# Lista de Produtos saindo em Alto Volume (nos pedidos do dia em questão)

# Lista de Pedidos

# Lista de Pontos de Venda

# Lista de Mensalistas

# Lista de Vendedores Externos

# Lista de Encomendas

# Lista de Encomendas ordenadas por Data de Entrega

# Lista de Entregadores

# Lista de Entregas

# Lista de Entregas Não Iniciadas

# Lista de Entregas Em Andamento

# Relatório do Ponto Eletrônico




# ROTAS DO ATENDENTE

# Lista de Pedidos

# Lista de Entregas

# Lista de Encomendas

# Lista de Entregadores




# ROTAS DO VENDEDOR EXTERNO

# Lista de Lojas Mensalistas




# ROTAS DO ENTREGADOR

# Lista de Entregas




# ROTAS DO CONFEITEIRO

# Lista de Receitas

# Lista de Encomendas

# Agendamento de Produção



from ..modelos import Pedido 


"""

Um pedido pode conter as seguintes informações
- unidade onde foi registrado
- ponto de venda onde foi registrado
- funcionário pelo qual foi registrado
- itens que compõem o pedido
- dia em que o pedido foi registrado
- se é para entrega
- valor total


######################################
######################################


FUNÇÕES DA BIBLIOTECA


IMPLEMENTADOS:

 

PARA IMPLEMENTAR:

Todos os pedidos
Todos os pedidos de uma unidade
Todos os pedidos de um ponto de venda

Todos os pedidos (paginados)
Todos os pedidos (paginados) de uma unidade
Todos os pedidos (paginados) de um ponto de venda

Todos os pedidos com entrega
Todos os pedidos com entrega de uma unidade 


Todos os pedidos com determinado item
Todos os pedidos com determinado item de uma unidade 
Todos os pedidos com determinado item de um ponto de venda 


Todos os pedidos de determinado dia
Todos os pedidos de determinado dia de uma unidade
Todos os pedidos de determinado dia de um ponto de venda
Todos os pedidos de determinado dia com entrega
Todos os pedidos de determinado dia de uma unidade com entrega
Todos os pedidos de determinado dia com determinado item


Todos os pedidos de determinado dia com determinado item de uma unidade
Todos os pedidos de determinado dia com determinado item de uma unidade com entrega


Todos os pedidos de determinado funcionario
Todos os pedidos de determinado funcionario de determinado dia
Todos os pedidos de determinado funcionario com entrega
Todos os pedidos de determinado funcionario com determinado item
Todos os pedidos de determinado funcionario 

"""



# Todos os pedidos
def lista_pedidos():
    pedidos = Pedido.query.order_by(
        Pedido.id.desc()
        ).all()

    return pedidos

def lista_pedidos_unidade(unidade_id):
    pedidos = Pedido.query.filter(
        Pedido.unidade_id == unidade_id
    ).all()
    return pedidos

def lista_pedidos_ponto_venda(ponto_de_venda_id):
    pedidos = Pedido.query.filter_by(ponto_de_venda_id=ponto_de_venda_id).all()
    return pedidos


# Todos os pedidos paginado
def lista_pedidos_paginado(pagina=1):
    pedidos = Pedido.query.order_by(
        Pedido.data_registro.desc()
        ).paginate(pagina, app.config['N_PEDIDOS_POR_PAGINA'], False)

    return pedidos

def lista_pedidos_unidade_paginado(unidade_id, pagina=1):
    pedidos = Pedido.query.filter(
        Pedido.unidade_id==unidade_id
        ).paginate(pagina, app.config['N_PEDIDOS_POR_PAGINA'], False)
        
    return pedidos

def lista_pedidos_ponto_venda_paginado(ponto_de_venda_id, pagina=1):
    pedidos = Pedido.query.filter_by(
        ponto_de_venda_id=ponto_de_venda_id
        ).paginate(pagina, app.config['N_PEDIDOS_POR_PAGINA'], False)
    return pedidos


# Consultando pedidos com entrega
def lista_pedidos_com_entrega():
    pedidos_com_entrega = Pedido.query.filter_by(para_entrega=True).all()
    return pedidos_com_entrega

def lista_pedidos_unidade_com_entrega(unidade_id):
    return 1


# Consultando pedidos com determinado item
def lista_pedidos_com_item(produto_id):
    return 1

def lista_pedidos_unidade_com_item(unidade_id, produto_id):
    return 1

def lista_pedidos_ponto_venda_com_item(ponto_venda_id, produto_id):
    return 1


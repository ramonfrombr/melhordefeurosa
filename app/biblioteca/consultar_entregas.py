from ..modelos import Entrega

"""



Todos as entregas de determinado dia
Todas as entregas de determinado dia de uma unidade
"""




# Todas as entregas
def lista_entregas():
    entregas = Entrega.query.order_by(
        Entrega.data_registro.desc()
        ).all()
    return entregas

# Todas as entregas de determinada unidade
def lista_entregas_unidade(unidade_id):
    return 1


# Todas as entregas de determinado entregador
def lista_entregas_entregador(entregador_id):
    return 1

# Todas as entregas não iniciadas
def lista_entregas_nao_iniciadas():
    entregas_nao_iniciadas = Entrega.query.order_by(
        Entrega.data_registro.desc()
        ).filter_by(status=0).all()
    return entregas_nao_iniciadas


# Todas as entregas não iniciadas por unidade
def lista_entregas_unidade_nao_iniciadas(unidade_id):
    return 1

# Todas as entregas não iniciadas por entregador
def lista_entregas_entregador_nao_iniciadas(entregador_id):
    return 1


# Todas as entregas em andamento
def lista_entregas_em_andamento():
    entregas_em_andamento = Entrega.query.order_by(
        Entrega.data_registro.desc()
        ).filter_by(status=1).all()
    return entregas_em_andamento

# Todas as entregas em andamento por unidade
def lista_entregas_unidade_em_andamento(unidade_id):
    return 1

# Todas as entregas em andamento por entregador
def lista_entregas_entregador_em_andamento(entregador_id):
    return 1

# Todas as entregas concluidas
def lista_entregas_concluidas():
    entregas_concluidas = Entrega.query.order_by(
        Entrega.data_registro.desc()
        ).filter_by(status=2).all()
    return entregas_concluidas

# Todas as entregas concluidas por unidade
# Todas as entregas concluidas por entregador




# Todas as entregas de determinado dia

# Todas as entregas de determinado dia por unidade

# Todas as entregas de determinado período

# Todas as entregas de determinado período por unidade

# Consultando entregas de uma unidade



def lista_entregas_unidade_nao_iniciadas(unidade_id):
    return 1

def lista_entregas_unidade_em_andamento(unidade_id):
    return 1

def lista_entregas_unidade_concluidas(unidade_id):
    return 1

# Consultando nº de entregas

def n_entregas():
    return 1

def n_entregas_nao_iniciadas():
    return 1

def n_entregas_em_andamento():
    return 1

def n_entregas_concluidas():
    return 1

# Consultando nº de entregas de uma unidade

def n_entregas_unidade(unidade_id):
    return 1

def n_entregas_unidade_nao_iniciadas(unidade_id):
    return 1

def n_entregas_unidade_em_andamento(unidade_id):
    return 1

def n_entregas_unidade_concluidas(unidade_id):
    return 1

import logging
from app import criar_app
from app import db
from app.modelos import PontoDeVenda, Unidade, Usuario, Pedido, Produto
from config import ConfiguracaoDesenvolvimento
import random
from faker import Faker

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

logging.getLogger().setLevel(logging.DEBUG)

log = logging.getLogger(__name__)

app = criar_app(ConfiguracaoDesenvolvimento)

app.app_context().push()

faker = Faker('pt_BR')



lista_palavras = [
    'sabor', 'prato', 'tradicional', 'doce', 'massa', 'assado',
    'melhor', 'ótimo', 'bom', 'sal', 'açucar', 'quente', 'frio',
    'gelado', 'gostoso', 'saboroso', 'cremoso', 'amor', 'sobremesa',
    'almoço', 'café da manhã', 'jantar', 'lanche', 'café da tarde'
]



def gerar_atendentes():
    return 1

def gerar_entregadores():
    return 1

def gerar_pedidos():
    return 1

def gerar_entregas():
    return 1


def generate_tags(n):

    tags = list()
    
    for i in range(n):

        tag = Tag()
        
        tag.title = faker.color_name()
        
        tags.append(tag)
        
        try:
            db.session.add(tag)
            db.session.commit()
        
        except Exception as e:

            log.error("Fail to add tag %s: %s" % (str(tag), e))
            
            db.session.rollback()
    
    return tags


def generate_users(n):

    users = list()

    for i in range(n):

        user = User()

        user.username = faker.name()
        
        user.password = "password"
        
        users.append(user)
        
        try:
            db.session.add(user)
            db.session.commit()

        except Exception as e:
            log.error("Fail to add user %s: %s" % (str(user), e))
            db.session.rollback()

    return users





def gerar_unidades(n=5):

    unidades = list()

    for i in range(n):

        unidade = Unidade(faker.city())

        unidades.append(unidade)

        try:
            db.session.add(unidade)
            db.session.commit()

        except Exception as excecao:

            log.error("Falha ao adicionar unidade: %s: %s", (str(unidade), excecao))

            db.session.rollback()
    
    return unidades


def gerar_pontos_venda(unidades, n=15):

    pontos_de_venda = list()

    for i in range(n):

        ponto = PontoDeVenda()
        
        ponto.nome = "Ponto de venda " + i

        ponto.local = faker.address()

        ponto.data_cadastro = faker.past_date()

        ponto.tipo_ponto_venda_id = random.randrange(0, 5)

        ponto.unidade_id = unidades[random.randrange(0, len(unidades))].id

        pontos_de_venda.append(ponto)

        try:
            db.session.add(ponto)
            db.session.commit()

        except Exception as excecao:
            log.error("Falha ao adicionar ponto de venda %s: %s" % (str(ponto), excecao))
            db.session.rollback()

    return pontos_de_venda




def gerar_pedidos(pontos_de_venda, n=100):

    for i in range(n):

        pedido = Pedido()

        pedido.comentario = faker.sentence(ext_word_list=lista_palavras).capitalize()

        pedido.data_registro = faker.past_date()
        
        #pedido.atendente_id = 

        ponto_de_venda = pontos_de_venda[random.randrange(0, len(pontos_de_venda))]

        pedido.unidade_id = ponto_de_venda.unidade_id
        
        pedido.ponto_de_venda_id = ponto_de_venda.id
        
        razao_entregas = [False, True, True]

        pedido.para_entrega = razao_entregas[random.randrange(0, len(razao_entregas))]
        
        if pedido.para_entrega == True:
            pedido.entrega_id = 1
        
        pedido.valor_total = 100



    



def generate_posts(users, tags, n=100):

    for i in range(n):

        post = Post()
        
        post.title = faker.sentence()
        
        post.text = faker.text(max_nb_chars=1000)

        post.publish_date = faker.date_this_century(before_today=True, after_today=False)
        
        post.user_id = users[random.randrange(0, len(users))].id

        post.tags = [tags[random.randrange(0, len(tags))] for i in range(0, 2)]
        
        try:
            db.session.add(post)
            db.session.commit()

        except Exception as e:
            log.error("Fail to add post %s: %s" % (str(post), e))
            db.session.rollback()





generate_posts(generate_users(10), generate_tags(5))

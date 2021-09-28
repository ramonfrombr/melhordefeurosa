from random import randint, randrange, choice
from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .modelos import Empresa, Unidade, PontoDeVenda, Usuario, Pedido, PrecoProduto, Produto, Entrega


# Lista de palavras relacionadas a um comentário em um pedido
lista_palavras_pedido = [
    'produto', 'preço', 'embalagem', 'comida', 'entrega', 'barato', 'caro', 'rápido', 'lento', 'loja', 'gerente', 'pedido', 'atendimento', 'atendente'
]

lista_palavras_entrega = ['rua', 'avenida', 'estrada', 'garagem', 'carro', 'prédio', 'calçada', 'quarteirão', 'caminhão', 'moto', 'semáforo', 'entrega', 'produto', 'embalagem', 'entregador', 'cliente']

lista_tipos_empresas = ['Padaria', 'Farmácia', 'Restaurante', 'Hospital', 'Faculdade', 'Bar', 'Loja de Roupas', 'Cinema', 'Shopping', 'Supermercados', 'Mercearia', 'Loja de Material de Construção', 'Barbearia', 'Salão de Beleza', 'Lanchonete', 'Distribuidora de Bebidas', ]



def gerar_conteudo_fake():

    usuarios_fake()

    empresas_fake()

    unidades_fake()

    precos_fake()

    pedidos_fake()

    



def usuarios_fake(n_usuarios=500):

    faker = Faker('pt_BR')

    """
        id
        nome
        sobrenome
        cpf
        rg
        data_nascimento
        nome_usuario
        senha
        empresa_id
        unidade_id
        unidade
        ponto_venda_id
        ponto_venda
        entregas_feitas
    """

    # Seleciona os ids de todas as empresas
    ids_empresas = [id for id, in db.session.query(Empresa.id)]

    # Repita
    for i in range(n_usuarios):

        usuario = Usuario()

        usuario.nome = faker.name()

        usuario.sobrenome = faker.name()

        usuario.nome_usuario = faker.user_name()

        usuario.senha = faker.password()


        """
        #if ids_empresas:
            

        # Seleciona o id de uma empresa aleatória
        id_empresa_aleatoria = choice(ids_empresas)

        # Atribui o id da empresa selecionada aleatóriamente
        usuario.empresa_id = id_empresa_aleatoria

        # Seleciona os ids das unidades da empresas aleatória selecionada anteriormente
        ids_unidades_da_empresa_aleatoria = [id for id, in db.session.query(Unidade.id).filter_by(empresa_id=id_empresa_aleatoria)]

        # Seleciona o id de uma unidade aleatória
        id_unidade_aleatoria = choice(ids_unidades_da_empresa_aleatoria)

        # Atribui o id de uma das unidades da empresa selecionada aleatóriamente
        usuario.unidade_id = id_unidade_aleatoria

        usuario.unidade = Unidade.query.filter_by(id=id_unidade_aleatoria).first()

        # Seleciona os ids dos pontos de venda da unidade aleatória selecionada
        ids_pontos_venda_da_empresa_aleatoria = [id for id, in db.session.query(PontoDeVenda.id).filter_by(unidade_id=id_unidade_aleatoria)]

        id_ponto_venda_aleatorio = choice(ids_pontos_venda_da_empresa_aleatoria)

        # Atribui o id do ponto de venda aleatório
        usuario.ponto_venda_id = id_ponto_venda_aleatorio 

        usuario.ponto_venda = PontoDeVenda.query.filter_by(id=id_ponto_venda_aleatorio ).first()
        """

        db.session.add(usuario)

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

def empresas_fake(n_empresas=100):
    
    """
            id
            razao_social
            nome_fantasia
            endereco
            codigo_postal
            tamanho
            data_inscricao
            data_fundacao
            nome_fundador
            email_contato
            segmento_id
            cidade_id
            estado_id
            pais_id
            admin_id
        """

    faker = Faker('pt_BR')

    for i in range(n_empresas):

        empresa = Empresa()

        nome_empresa = choice(lista_tipos_empresas) + " " + faker.company()

        empresa.razao_social = nome_empresa

        empresa.nome_fantasia = nome_empresa

        empresa.endereco = faker.address()

        empresa.codigo_postal = randint(1000000, 9999999)

        empresa.tamanho = randint(1, 3)

        empresa.data_inscricao = faker.past_date()

        empresa.email_contato = faker.email()

        empresa.data_fundacao = faker.past_date()

        empresa.nome_fundador = faker.name()

        # Seleciona os ids dos usuários que não possuem empresa
        ids_usuarios = [id for id, in db.session.query(Usuario.id).filter_by(empresa_id=None)]

        id_usuario_aleatorio = choice(ids_usuarios)

        empresa.admin_id = id_usuario_aleatorio

        db.session.add(empresa)

        try:
            db.session.commit()

            # Atualiza o usuário
            usuario = Usuario.query.filter_by(id=id_usuario_aleatorio).first()

            usuario.empresa_id = empresa.id

            db.session.add(usuario)

            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
        except IntegrityError:
            db.session.rollback()

def unidades_fake(n_unidades=100):

    """
        id
        nome
        cidade
        bairro
        endereco
        data_cadastro
        empresa_id
        gerente_id
    """

    faker = Faker('pt_BR')

    # Seleciona os ids de todas as empresas
    ids_empresas = [id for id, in db.session.query(Empresa.id)]

    for i in range(n_unidades):

        unidade = Unidade()

        unidade.nome = "Unidade " + faker.city()

        unidade.endereco = faker.address()

        unidade.data_cadastro = faker.past_date()

        # Seleciona o id de uma empresa aleatoriamente
        id_empresa_aleatoria = choice(ids_empresas)

        # Define o id da empresa da unidade
        unidade.empresa_id = id_empresa_aleatoria

        # Seleciona os ids dos usuários da empresa aleatória
        ids_usuarios_empresa_aleatoria = [id for id, in db.session.query(Usuario.id).filter_by(empresa_id=id_empresa_aleatoria).all()]

        unidade.gerente_id = choice(ids_usuarios_empresa_aleatoria)

        db.session.add(unidade)

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

def pedidos_fake(n_pedidos=100):

    """
        id
        itens
        comentario
        data_registro
        atendente_id
        atendente
        cliente_id
        cliente
        unidade_id
        ponto_venda_id
        empresa_id
        para_entrega
        entrega_id
        valor_total
    """

    faker = Faker('pt_BR')

    produtos = Produto.query.all()

    for i in range(n_pedidos):

        pedido = Pedido()

        pedido.valor_total = 0

        # Define o número de produtos
        n_produtos = randint(2, 5)

        # Repita
        for i in range(n_produtos):

            # Escolha um produto aleatoriamente
            produto = choice(produtos)

            # Adicione o produto à lista de itens do pedido
            pedido.itens.append(produto)

            # Seleciona o último preco atribuido ao produto
            preco_produto = PrecoProduto.query.filter_by(produto_id=produto.id).order_by(PrecoProduto.id.desc()).first()

            if preco_produto:
                # Adiciona o preço do produto ao valor total do pedido
                pedido.valor_total += preco_produto.valor
            

        pedido.comentario = faker.sentence(ext_word_list=lista_palavras_pedido).capitalize()

        pedido.data_registro = faker.past_date()

        ids_usuarios = [id for id, in db.session.query(Usuario.id)]

        id_cliente_aleatorio = choice(ids_usuarios)

        pedido.cliente_id = id_cliente_aleatorio
        
        pedido.cliente = Usuario.query.filter_by(id=id_cliente_aleatorio).first()
        

        id_atendente_aleatorio = choice(ids_usuarios)

        pedido.atendente_id = id_atendente_aleatorio
        
        pedido.atendente = Usuario.query.filter_by(id=id_atendente_aleatorio).first()
        
        pedido.unidade_id = pedido.atendente.unidade_id
        
        pedido.ponto_venda_id = pedido.atendente.ponto_venda_id
        
        pedido.empresa_id = pedido.atendente.empresa_id
        
        # A cada 3 pedidos, 1 possui entrega
        pedido.para_entrega = choice([False, False, True])
        
        db.session.add(pedido)

        try:
            db.session.commit()

            # Se o pedido for para entrega
            if (pedido.para_entrega):

                # Crie uma entrega

                entrega = Entrega()

                """
                    id
                    data_registro
                    destino
                    cliente_nome
                    cliente_whatsapp
                    status
                    pedido_id
                    entregador_id
                    unidade_id
                """

                entrega.data_registro = faker.past_date()

                entrega.destino = faker.address()

                entrega.cliente_nome = faker.name()

                entrega.cliente_whatsapp = faker.phone_number()
                
                entrega.status = choice([1, 2, 3])

                # A entrega ainda não existe, portanto não tem como selecionar o id do pedido
                #entrega.pedido_id

                # !!! ESTA CONSULTA NÃO ESTÁ SELECIONANDO OS USUÁRIOS COM ROLE ENTREGADOR CORRETAMENTE
                ids_entregadores_da_unidade = [id for id, in db.session.query(Usuario.id).filter_by(unidade_id=pedido.unidade_id)]

                entrega.entregador_id = choice(ids_entregadores_da_unidade)

                entrega.unidade_id = pedido.unidade_id

                db.session.add(entrega)

                try:
                    db.session.commit()

                except IntegrityError:
                    db.session.rollback()

        except IntegrityError:
            db.session.rollback()

def precos_fake():

    """
        id
        produto_id
        valor
        data_inicio
        data_fim
        descricao
        ponto_venda_id
        unidade_id
        empresa_id
    """

    # Seleciona todos os produtos
    produtos = Produto.query.all()

    # Seleciona todas as unidades
    unidades = Unidade.query.all()

    # Para cada produto
    for produto in produtos:

        # Para cada unidade
        for unidade in unidades:

            # Cria dois precos para o produto vinculando a unidade
            for i in range(2):
                
                preco = PrecoProduto()

                preco.produto_id = produto.id

                preco.valor = randrange(100,999)

                preco.unidade_id = unidade.id

                preco.empresa_id = unidade.empresa_id

                db.session.add(preco)

                try:
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()



def gerentes_fake(n_gerentes=10):
    return 1

def atendentes_fake(n_atendentes=10):
    return 1

def entregadores_fake(n_entregadores=10):
    return 1

def pontos_venda_fake(n_pontos_venda=15):
    return 1

def entregas_fake(n_entregas=50):
    return 1


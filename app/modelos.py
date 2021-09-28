from re import M
from . import db
import datetime

# DOCUMENTAÇÃO

"""
    Lista de Modelos:

    CompraMaterial
    Encomenda
    Entrega
    Equipamento
    Material
    Notificacao
    Pedido
    PontoDeVenda
    PrecoProduto
    Producao
    Produto
    Usuario
    Unidade
    TipoPontoDeVenda
"""

"""
    Nos modelos que possuem chaves estrangeiras (foreign key), as propriedades 'use_alter' e 'name' foram adicionadas para lidar com um erro de "referência circular"
"""

# Itens de cada pedido
pedidos_itens = db.Table('pedidos_itens',

    db.Column('pedido_id', db.Integer, db.ForeignKey('pedidos.id')),

    db.Column('produto_id', db.Integer, db.ForeignKey('produtos.id')),

    # Preço do produto no dia que o pedido foi registrado
    db.Column('preco_data', db.Float),

    # Quantas unidades do produto
    db.Column('quantidade', db.Integer, default=1)
)

# Ingredientes de cada produto
produtos_materiais = db.Table('produtos_materiais',

    db.Column('produto_id', db.Integer, db.ForeignKey('produtos.id')),

    db.Column('material_id', db.Integer, db.ForeignKey('materiais.id')),

    # Preço do produto no dia que o pedido foi registrado
    db.Column('material_quantidade', db.Integer, nullable=False),

    # Tipo quantidade
    # 1 - unidade
    # 2 - grama
    # 3 - kilograma
    # 4 - mililitros
    # 5 - litros
    db.Column('unidade_medida', db.Integer, nullable=False)
)




class Continente(db.Model):
    
    __tablename__ = 'continentes'
    
    """
    América do Norte
    América Central
    América do Sul

    Europa
    Ásia
    África
    Oceania

    """

    id = db.Column(db.Integer(), primary_key=True)

    nome = db.Column(db.String(32))

    @staticmethod
    def adicionar_continentes():

        continentes = [
            {'nome': "América do Norte", },
            {'nome': "América do Sul", },
            {'nome': "América Central", },
            {'nome': "Europa Latina", },
            {'nome': "Europa Germânica", },
            {'nome': "Europa Nórdica", },
            {'nome': "Leste da Europa", },
            {'nome': "Europa Central", },
            {'nome': "Balcãs", },
            {'nome': "Norte da África", },
            {'nome': "África Subsaariana", },
            {'nome': "Oriente Médio ", },
            {'nome': "Região onde fica Iran, Pakistão, Afeganistão", },
            {'nome': "Região onde fica Kirghistão, Tajikstão, etc", },
            {'nome': "Subcontinente Indiano", },
            {'nome': "Sudoeste Asiático", },
            {'nome': "Extremo Oriente", },
            {'nome': "Oceania", },
        ]

        # Para cada continente
        for c in continentes:

            # Consulte o continente
            continente = Continente.query.filter_by(nome=c['nome']).first()


            # Se não houver um continente com o nome pesquisado
            if continente is None:

                # Crie um continente com o nome em questão
                continente = Continente(nome=c['nome'])

            # Adicione o continente à sessão
            db.session.add(continente)

        # Salve a sessão
        db.session.commit()


class Pais(db.Model):

    __tablename__ = 'paises'

    id = db.Column(db.Integer(), primary_key=True)

    nome = db.String(db.String(128))

    nome_completo = db.String(db.String(128))

    continente_id = db.Column(db.Integer(), db.ForeignKey('continentes.id'))


# Estado, província, etc
class Estado(db.Model):

    __tablename__ = 'estados'

    id = db.Column(db.Integer(), primary_key=True)

    nome = db.String(db.String(128))

    
    pais_id = db.Column(db.Integer(), db.ForeignKey('paises.id'))
    continente_id = db.Column(db.Integer(), db.ForeignKey('continentes.id'))


class Cidade(db.Model):

    __tablename__ = 'cidades'

    id = db.Column(db.Integer(), primary_key=True)

    nome = db.String(db.String(128))

    estado_id = db.Column(db.Integer(), db.ForeignKey('estados.id'))
    pais_id = db.Column(db.Integer(), db.ForeignKey('paises.id'))
    continente_id = db.Column(db.Integer(), db.ForeignKey('continentes.id'))


class Bairro(db.Model):

    __tablename__ = 'bairros'

    id = db.Column(db.Integer(), primary_key=True)

    nome = db.String(db.String(128))

    cidade_id = db.Column(db.Integer(), db.ForeignKey('cidades.id'))
    estado_id = db.Column(db.Integer(), db.ForeignKey('estados.id'))
    pais_id = db.Column(db.Integer(), db.ForeignKey('paises.id'))
    continente_id = db.Column(db.Integer(), db.ForeignKey('continentes.id'))









# Compra de material/estoque
class CompraMaterial(db.Model):

    __tablename__ = 'compra_material'

    id = db.Column(db.Integer(), primary_key=True)

    material_id = db.Column(db.Integer(), db.ForeignKey('materiais.id'))

    valor_compra = db.Column(db.Float(), nullable=False)

    quantidade = db.Column(db.Float())
    
    # 1 - unidades
    # 2 - kilograma
    # 3 - litro
    unidade_medida = db.Column(db.Integer()) 
    
    data_compra = db.Column(db.Date, default=datetime.datetime.now)

    data_vencimento = db.Column(db.Date)

    marca = db.Column(db.String(32))

    fornecedor = db.Column(db.String(64))
    fornecedor_telefone = db.Column(db.String(32))

    unidade_id = db.Column(db.Integer(), db.ForeignKey('unidades.id'))
    empresa_id = db.Column(db.Integer(), db.ForeignKey('empresas.id'))

# Empresa
class Empresa(db.Model):

    __tablename__ = 'empresas'

    """
    id
    razao_social
    nome_fantasia
    endereco
    codigo_postal
    tamanho
    data_inscricao
    data_fundacao
    segmento_id
    cidade_id
    estado_id
    pais_id
    admin_id
    """

    id = db.Column(db.Integer(), primary_key=True)

    razao_social = db.Column(db.String(128))

    nome_fantasia = db.Column(db.String(128))

    endereco = db.Column(db.String(255))
    
    codigo_postal = db.Column(db.String(64))

    # 1 - Pequeno porte 2 - Médio porte 3 - Grande porte
    tamanho = db.Column(db.Integer())

    data_inscricao = db.Column(db.DateTime(), default=datetime.datetime.now)

    data_fundacao = db.Column(db.Date())

    nome_fundador = db.Column(db.String(128))

    email_contato = db.Column(db.String(128))

    segmento_id = db.Column(db.Integer(), db.ForeignKey('segmentos_empresas.id'))

    bairro_id = db.Column(db.Integer(), db.ForeignKey('bairros.id'))

    cidade_id = db.Column(db.Integer(), db.ForeignKey('cidades.id'))

    estado_id = db.Column(db.Integer(), db.ForeignKey('estados.id'))

    pais_id = db.Column(db.Integer(), db.ForeignKey('paises.id'))

    admin_id = db.Column(db.Integer(), db.ForeignKey('usuarios.id'))

# Encomendas registradas
class Encomenda(db.Model):

    __tablename__ = 'encomendas'

    id = db.Column(db.Integer(), primary_key=True)

    data_registro = db.Column(db.DateTime(), default=datetime.datetime.now)

    nome_cliente = db.Column(db.String(32))

    data_entrega = db.Column(db.DateTime())

    endereco_entrega = db.Column(db.String(255))

    descricao = db.Column(db.String(255))

    unidade_id = db.Column(db.Integer(), db.ForeignKey('unidades.id'))

    itens = db.relationship(
        'Producao',
        backref='encomenda',
        lazy='dynamic'
    )

# Entregas de pedidos
class Entrega(db.Model):

    __tablename__ = 'entregas'

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

    id = db.Column(db.Integer(), primary_key=True)

    data_registro = db.Column(db.DateTime(), default=datetime.datetime.now)

    # Endereço e nome do cliente
    destino = db.Column(db.String(64))

    cliente_nome = db.Column(db.String(32))
    cliente_whatsapp = db.Column(db.String(32))

    # Status 0 - Não iniciada
    # Status 1 - Em andamento
    # Status 2 - Concluida
    status = db.Column(db.Integer(), default=0)

    pedido_id = db.Column(db.Integer(), db.ForeignKey('pedidos.id', use_alter=True, name='fk_pedidos_id'))


    atendente_id = db.Column(db.Integer(), db.ForeignKey('usuarios.id', use_alter=True, name='fk_usuarios_id'))
    
    atendente = db.relationship(
        'Usuario',
        foreign_keys=atendente_id,
        backref=db.backref('entregas_registradas', order_by=id))





    entregador_id = db.Column(db.Integer(), db.ForeignKey('usuarios.id', use_alter=True, name='fk_usuarios_id'))

    entregador = db.relationship(
        'Usuario',
        foreign_keys=entregador_id,
        backref=db.backref('entregas_feitas', order_by=id))


    unidade_id = db.Column(db.Integer(), db.ForeignKey('unidades.id', use_alter=True, name='fk_unidades_id'))






    def atribuir_entregador(usuario_id):
        return 1

    def enviar_msg_wpp_cliente(cliente_whatsapp, mensagem):
        return 1



    def __init__(self, destino=""):
        self.destino = destino
    
    def __repr__(self):
        return "<Entrega #{}>".format(self.nome)

# Equipamento das unidades
class Equipamento(db.Model):

    __tablename__ = 'equipamentos'

    # Lista de Equipamentos
    """
        Fogão
        Forno
        Estufa Espositora
        Mesa
        Liquidificador
        Carrinho
        Bicicleta Cargueira 
        Cesto de Palha
        Barril de Plástico com Torneira (12 litros)
        Caixa de Plástico com Tampa
        Forma para 4 Pães Caseiro
        Quadro Negro Grande
        Quadro Negro Pequeno
    """

    id = db.Column(db.Integer(), primary_key=True)

    nome = db.Column(db.String(64), nullable=False)

    data_compra = db.Column(db.Date(), default=datetime.datetime.now)

    unidade_id = db.Column(db.Integer(), db.ForeignKey('unidades.id'))

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return "<Equipamento '{}'>".format(self.nome)

# Marca de um produto
class Marca(db.Model):

    __tablename__ = 'marcas'

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(128))

    empresa_id = db.Column(db.Integer(), db.ForeignKey('empresas.id'))

    #produtos

# Estoque de ingredientes, descartáveis e outros materiais usados na produção de um produto
class Material(db.Model):

    __tablename__ = 'materiais'

    # Lista de Materiais
    """
        Trigo
        Açúcar Branco
        Margarina (80% lipídios)
        Óleo de Soja
        Sal 
        Ovo
        Fermento Granulado

        Frango
        Tomate
        Cebola

        Coloral
        Orégano
        Alho
        
        Vinagre
        Creme de Leite

        Forma de Alumínio Descartável para Empadinha (50ml)
        Sacola de Papel para Embalar Empadinha
        Bandeja de Isopor (para 6 empadinhas)
        Sacola para Embalar Bandeja de Empadas
        Sacola para Embalar Pão (22cm x 46cm)
        Arame Plastificado para Embalagem
    """

    id = db.Column(db.Integer(), primary_key=True)

    nome = db.Column(db.Integer(), nullable=False)

    descricao = db.Column(db.String(255))

    quantidade = db.Column(db.Float())

    # 1 - unidades
    # 2 - kilogramas
    # 3 - litros
    quantidade_tipo = db.Column(db.Integer())


    tipo_id = db.Column(db.Integer(), db.ForeignKey('tipos_de_material.id'))

    @staticmethod
    def inserir_materiais():

        materiais = [
            {'nome': "Trigo", 'descricao': ""},
            {'nome': "Açúcar Branco", 'descricao': ""},
            {'nome': "Margarina (80% lipídios)", 'descricao': ""},
            {'nome': "Óleo de Soja", 'descricao': ""},
            {'nome': "Sal Refinado", 'descricao': ""},
            {'nome': "Ovo", 'descricao': ""},
            {'nome': "Fermento Granulado", 'descricao': ""},
            {'nome': "Frango", 'descricao': ""},
            {'nome': "Tomate", 'descricao': ""},
            {'nome': "Cebola", 'descricao': ""},
            {'nome': "Coloral", 'descricao': ""},
            {'nome': "Orégano", 'descricao': ""},
            {'nome': "Alho", 'descricao': ""},
            {'nome': "Vinagre", 'descricao': ""},
            {'nome': "Creme de Leite", 'descricao': ""},
            {'nome': "Forma de Alumínio Descartável para Empadinha (50ml)", 'descricao': ""},
            {'nome': "Sacola de Papel para Embalar Empadinha", 'descricao': ""},
            {'nome': "Bandeja de Isopor (para 6 empadinhas)", 'descricao': ""},
            {'nome': "Sacola para Embalar Bandeja de Empadas", 'descricao': ""},
            {'nome': "Sacola para Embalar Pão (22cm x 46cm)", 'descricao': ""},
            {'nome': "Arame Plastificado para Embalagem", 'descricao': ""},
        ]

        # Para cada material
        for m in materiais:

            # Consulte o material
            material = Material.query.filter_by(nome=m['nome']).first()


            # Se não houver um material com o nome pesquisado
            if material is None:

                # Crie um material com o nome em questão
                material = Material(nome=m['nome'], descricao=m['descricao'])

            # Adicione o material à sessão
            db.session.add(material)

        # Salve a sessão
        db.session.commit()

    def __init__(self, nome, descricao=""):
        self.nome = nome
        self.descricao = descricao

    def __repr__(self):
        return "<Material '{}'>".format(self.nome)    
    
# Notificações do sistema para o funcionário
class Notificacao(db.Model):

    __tablename__ = 'notificacoes'

    id = db.Column(db.Integer(), primary_key=True)

    usuario_id = db.Column(db.Integer(), db.ForeignKey('usuarios.id'))

    empresa_id = db.Column(db.Integer(), db.ForeignKey('empresas.id', use_alter=True, name='fk_empresas_id'))

    titulo = db.Column(db.String(64))

    conteudo = db.Column(db.String(255))

    data_registro = db.Column(db.DateTime(), default=datetime.datetime.now)
    
    data_aberta = db.Column(db.DateTime())

    # 0 - Não aberta
    # 1 - Aberta
    # 2 - Confirmada (para quando a notificacao pede ao funcionario para confirmar algo, como a conclusao de uma entrega para os entregadores)
    status = db.Column(db.Integer())

    # Aviso de nova entrega
    # Atraso na entrega
    # Confirmação de conclusão de entrega
    tipo = db.Column(db.Integer())

# Pedidos registrados
class Pedido(db.Model):
    
    __tablename__ = 'pedidos'
    
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

    id = db.Column(db.Integer(), primary_key=True)

    itens = db.relationship(

        'Produto',
        secondary=pedidos_itens,
        backref=db.backref('pedidos', lazy='dynamic')
    )

    comentario = db.Column(db.String(255))

    data_registro = db.Column(db.DateTime(), default=datetime.datetime.now)



    atendente_id = db.Column(db.Integer(), db.ForeignKey('usuarios.id', use_alter=True, name='fk_usuarios_id'))
    
    atendente = db.relationship(
        'Usuario',
        foreign_keys=atendente_id,
        backref=db.backref('pedidos_registrados', order_by=id))



    cliente_id = db.Column(db.Integer(), db.ForeignKey('usuarios.id', use_alter=True, name='fk_usuarios_id'))

    cliente = db.relationship(
        'Usuario',
        foreign_keys=cliente_id,
        backref=db.backref('pedidos_feitos', order_by=id))



    unidade_id = db.Column(db.Integer(), db.ForeignKey('unidades.id', use_alter=True, name='fk_unidades_id'))

    ponto_venda_id = db.Column(db.Integer(), db.ForeignKey('pontos_de_venda.id', use_alter=True, name='fk_pontos_de_venda_id'))

    empresa_id = db.Column(db.Integer(), db.ForeignKey('empresas.id', use_alter=True, name='fk_empresas_id'))



    para_entrega = db.Column(db.Boolean(), default=False)

    entrega_id = db.Column(db.Integer(), db.ForeignKey('entregas.id', use_alter=True, name='fk_entregas_id'))

    valor_total = db.Column(db.Float())



    # Imprime o nome e o preço dos itens do pedido
    def imprimir_preco_itens(self):

        # Para cada item do pedido
        for item in self.itens:
            

            # Seleciona o valor do item
            valor_do_item = PrecoProduto.query.filter_by(produto_id=item.id).first()

            # Imprime o nome do item e o valor
            print(f"{item.nome}: {valor_do_item}")

    # Calcula o valor total do pedido e atualiza o valor no objeto
    def calcular_valor_total(self):

        valor_total = 0

        # Para cada item do pedido
        for item in self.itens:
            
            # Seleciona o valor do item
            # (!!!) A CONSULTA ESTÁ SELECIONANDO ÚLTIMO PREÇO INSERIDO (ATRAVÉS DO ID DO PRODUTO) E NÃO A ÚLTIMA DATA VÁLIDA PARA O PREÇO
            valor_do_item = PrecoProduto.query.filter_by(produto_id=item.id).order_by(PrecoProduto.id.desc()).first()

            valor_total += valor_do_item

        # Define o valor total do pedido como sendo a soma dos preços dos produtos
        self.valor_total = valor_total

    def __init__(self, comentario=""):
        self.comentario = comentario

    def __repr__(self):
        return "<Pedido #{}>".format(self.id)

# Pontos de venda
class PontoDeVenda(db.Model):

    __tablename__ = 'pontos_de_venda'

    id = db.Column(db.Integer(), primary_key=True)

    nome = db.Column(db.String(32), nullable=False, unique=True)

    local = db.Column(db.String(64))
    
    data_cadastro = db.Column(db.Date(), default=datetime.datetime.now)

    tipo_ponto_venda_id = db.Column(db.Integer(), db.ForeignKey('tipos_ponto_venda.id'))

    gerente_id = db.Column(db.Integer(), db.ForeignKey('usuarios.id'))

    unidade_id = db.Column(db.Integer(), db.ForeignKey('unidades.id'))

    empresa_id = db.Column(db.Integer(), db.ForeignKey('empresas.id'))

    pedidos = db.relationship(
        'Pedido',
        backref='ponto_de_venda',
        lazy='dynamic'
    )


    def __init__(self, nome="Ponto De Venda Sem Nome"):
        self.nome = nome
    
    def __repr__(self):
        return "<Ponto de Venda '{}'>".format(self.nome)

# Histório de preços dos produtos vendidos
class PrecoProduto(db.Model):

    __tablename__ = 'precos_produtos'

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

    # Id do preço
    id = db.Column(db.Integer(), primary_key=True)
    
    # Id do produto
    produto_id = db.Column(db.Integer(), db.ForeignKey('produtos.id'))
    
    # Valor do produto em reais
    valor = db.Column(db.Float(), nullable=False)
    
    # Data de início de cobrança do preço sobre o produto
    data_inicio = db.Column(db.Date(), default=datetime.datetime.now)
    
    # Data de fim de cobrança do preço sobre o produto
    data_fim = db.Column(db.Date())
    
    # Descrição sobre o preço do produto
    descricao = db.Column(db.String(255))

    # Id do ponto de venda onde o preço foi aplicado
    ponto_venda_id = db.Column(db.Integer(), db.ForeignKey('pontos_de_venda.id'))

    # Id da unidade onde o preço foi aplicado
    unidade_id = db.Column(db.Integer(), db.ForeignKey('unidades.id'))

    # Id da empresa onde o preço foi aplicado
    empresa_id = db.Column(db.Integer(), db.ForeignKey('empresas.id'))


    def __init__(self, valor=0):
        self.valor = valor


    def __repr__(self):
        return "<Preço $'{}'>".format(self.valor)

# Registro de produção dos produtos vendidos (pão, empada, etc)
class Producao(db.Model):

    __tablename__ = 'producao'

    id = db.Column(db.Integer(), primary_key=True)

    quantidade = db.Column(db.Integer())

    data_producao = db.Column(db.DateTime(), default=datetime.datetime.now)

    produto_id = db.Column(db.Integer(), db.ForeignKey('produtos.id'))

    cozinheiro_id = db.Column(db.Integer(), db.ForeignKey('usuarios.id'))

    para_encomenda = db.Column(db.Boolean(), default=False)

    encomenda_id = db.Column(db.Integer(), db.ForeignKey('encomendas.id'))

    unidade_id = db.Column(db.Integer(), db.ForeignKey('unidades.id'))

# Lista de produtos vendidos
class Produto(db.Model):

    __tablename__ = 'produtos'

    # Lista de Produtos
    """
        Pão Caseiro Grande
        Pão Caseiro Pequeno
        Pão Francês
        Empadinha
        Coxinha
        Enroladinho
        Quibe
        Pastel

        Água
        Suco 150ml
        Café 150ml
        Café com Leite 200ml
        Capuccino



        Churrasquinho


        Sonho
        Donut
    """

    id = db.Column(db.Integer(), primary_key=True)

    nome = db.Column(db.String(64), nullable=False)

    descricao = db.Column(db.String(255))

    marca_id = db.Column(db.Integer(), db.ForeignKey('marcas.id'))



    # Restaurante, ateliês, e outros estabelecimentos cujos produtos são confeccionados
    materiais = db.relationship(
        'Material',
        secondary=produtos_materiais,
        backref=db.backref('produtos', lazy='dynamic')
    )

    historico_precos = db.relationship(
        'PrecoProduto',
        backref='produto',
        lazy='dynamic'
    )

    @staticmethod
    def inserir_produtos():

        # lista de produtos (lista de maps)
        # {'nome': "", 'descricao': ""}
        produtos = [
            {'nome': "Pão Caseiro Grande", 'descricao': "Pão caseiro tradicional com cerca de 400 gramas"},
            {'nome': "Empadinha de Frango", 'descricao': "Empadinha de frango com molho de tomate e cebola"},
            {'nome': "Suco 150ml", 'descricao': "Suco Natural em Copo Descartável de 150ml"},
            {'nome': "Pão Caseiro Pequeno", 'descricao': ""},
            {'nome': "Pão Francês", 'descricao': ""},
            {'nome': "Empadinha", 'descricao': ""},
            {'nome': "Coxinha", 'descricao': ""},
            {'nome': "Enroladinho", 'descricao': ""},
            {'nome': "Quibe", 'descricao': ""},
            {'nome': "Pastel", 'descricao': ""},
            {'nome': "Água", 'descricao': ""},
            {'nome': "Suco 150ml", 'descricao': ""},
            {'nome': "Café 150ml", 'descricao': ""},
            {'nome': "Café com Leite 200ml", 'descricao': ""},
            {'nome': "Capuccino", 'descricao': ""}
        ]

        # Para cada produto
        for p in produtos:

            # Consulte o banco de dados produrando por um produto que tenha o nome igual a um dos produtos definidos na lista de produtos
            produto = Produto.query.filter_by(nome=p['nome']).first()

            if produto is None:
            
                produto = Produto(nome=p['nome'], descricao=p['descricao'])

            db.session.add(produto)
        
        db.session.commit()

    def selecionar_preco(self):
    
        # Seleciona o último preco atribuido ao produto
        # (!!!) A CONSULTA NÃO SELECIONA O PRECO DE UMA UNIDADE/EMPRESA ESPECÍFICA
        ultimo_preco = PrecoProduto.query.filter_by(id=self.id).order_by(PrecoProduto.id.desc()).first()

        return ultimo_preco

    def __init__(self, nome="", descricao=""):
        self.nome = nome
        self.descricao = descricao

    def __repr__(self):
        return "<Produto '{}'>".format(self.nome)


class SegmentoEmpresa(db.Model):

    __tablename__ = 'segmentos_empresas'

    id = db.Column(db.Integer(), primary_key=True)

    nome = db.Column(db.String(128))

# Unidades
class Unidade(db.Model):

    __tablename__ = 'unidades'

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

    id = db.Column(db.Integer(), primary_key=True)

    nome = db.Column(db.String(32), nullable=False, unique=True)

    endereco = db.Column(db.String(32))

    bairro_id = db.Column(db.Integer(), db.ForeignKey('bairros.id'))

    cidade_id = db.Column(db.Integer(), db.ForeignKey('cidades.id'))

    estado_id = db.Column(db.Integer(), db.ForeignKey('estados.id'))

    pais_id = db.Column(db.Integer(), db.ForeignKey('paises.id'))
    

    data_cadastro = db.Column(db.Date(), default=datetime.datetime.now)


    empresa_id = db.Column(db.Integer(), db.ForeignKey('empresas.id', use_alter=True, name='fk_empresas_id'))

    gerente_id = db.Column(db.Integer(), db.ForeignKey('usuarios.id', use_alter=True, name='fk_usuarios_id'))


    pedidos = db.relationship(
        'Pedido',
        backref='unidade',
        lazy='dynamic'
    )

    entregas = db.relationship(
        'Entrega',
        backref='unidade',
        lazy='dynamic'
    )

    pontos_de_venda = db.relationship(
        'PontoDeVenda',
        backref='unidade',
        lazy='dynamic'
    )

    equipamentos = db.relationship(
        'Equipamento',
        backref='unidade',
        lazy='dynamic'
    )

    def __init__(self, nome="Unidade Sem Nome Definido"):
        self.nome = nome

    def __repr__(self):
        return "<Unidade '{}'>".format(self.nome)

# Usuários do web app
class Usuario(db.Model):

    __tablename__ = 'usuarios'

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

    id = db.Column(db.Integer(), primary_key=True)

    nome = db.Column(db.String(32))
    sobrenome = db.Column(db.String(64))
    cpf = db.Column(db.String(11))
    rg = db.Column(db.String(7))
    data_nascimento = db.Column(db.Date())

    nome_usuario = db.Column(db.String(255), nullable=False, unique=True)
    senha = db.Column(db.String(255))


    empresa_id = db.Column(
        db.Integer(),
        db.ForeignKey(
            'empresas.id',
            use_alter=True,
            name='fk_unidades_id'))

    unidade_id = db.Column(
        db.Integer(),
        db.ForeignKey(
            'unidades.id',
            use_alter=True,
            name='fk_unidades_id'))

    unidade = db.relationship(
        'Unidade',
        backref='funcionarios',
        foreign_keys=[unidade_id])

    ponto_venda_id = db.Column(
        db.Integer(),
        db.ForeignKey(
            'pontos_de_venda.id',
            use_alter=True,
            name='fk_ponto_venda_id'))

    ponto_de_venda = db.relationship(
        'PontoDeVenda',
        backref='funcionarios',
        foreign_keys=[ponto_venda_id])



    def __init__(self, nome_usuario=""):
        self.nome_usuario = nome_usuario
    
    def __repr__(self):
        return "<Usuário '{}'>".format(self.nome_usuario)


class TipoDeMaterial(db.Model):

    __tablename__ = 'tipos_de_material'

    id = db.Column(db.Integer(), primary_key=True)

    """
    Alimento
    Embalagem
    Limpeza
    """
    nome = db.Column(db.String(128))


# Tipos de Ponto de Venda
class TipoPontoDeVenda(db.Model):

    __tablename__ = 'tipos_ponto_venda'

    id = db.Column(db.Integer(), primary_key=True)

    nome = db.Column(db.String(32), nullable=False, unique=True)

    descricao = db.Column(db.String(255))

    pontos_associados = db.relationship(
        'PontoDeVenda',
        backref='tipo_ponto_venda',
        lazy='dynamic'
    )


    @staticmethod
    def inserir_tipos_ponto_venda():

        tipos = [
            {'nome': "Loja", 'descricao': ""},
            {'nome': "Tenda", 'descricao': ""},
            {'nome': "Carrinho", 'descricao': ""},
            {'nome': "Bicicleta Cargueira", 'descricao': ""}
        ]

        # Para cada tipo de ponto de venda
        for t in tipos:

            # Consulta o tipo
            tipo = TipoPontoDeVenda.query.filter_by(nome=t['nome']).first()

            # Se não houver um tipo com o nome pesquisado
            if tipo is None:

                # Crie esse tipo
                tipo = TipoPontoDeVenda(nome=t['nome'], descricao=t['descricao'])

            # Adicione à sessão
            db.session.add(tipo)

        # Salve a sessão
        db.session.commit()


    

    def __init__(self, nome, descricao=""):
        self.nome = nome
        self.descricao = descricao
    
    def __repr__(self):
        return "<Tipo de Ponto de Venda '{}'>".format(self.nome)


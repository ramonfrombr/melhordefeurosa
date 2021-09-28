from app.modelos import db, CompraMaterial, Empresa, Encomenda, Entrega, Equipamento, Material, Notificacao, Pedido, pedidos_itens, PontoDeVenda, PrecoProduto, Producao, Produto, Unidade, Usuario, TipoPontoDeVenda

from app.modelos import Continente, Pais, Estado, Cidade, Bairro

from app import migrate

from main import app

from app.biblioteca.consultar_pedidos import lista_pedidos



def reinicializar():

    db.drop_all()

    db.create_all()

    Continente.adicionar_continentes()

    #Pais.adicionar_paises()

    #Estado.adicionar_estados()

    #Cidade.adicionar_cidades()

    #Bairro.adicionar_bairros()

    Produto.inserir_produtos()

    Material.inserir_materiais()

    TipoPontoDeVenda.inserir_tipos_ponto_venda()



@app.shell_context_processor
def criar_contexto_shell():

    return dict(
        app=app,
        db=db,
        Bairro=Bairro,
        Cidade=Cidade,
        CompraMaterial=CompraMaterial,
        Continente=Continente,
        Empresa=Empresa,
        Encomenda=Encomenda,
        Entrega=Entrega,
        Equipamento=Equipamento,
        Estado=Estado,
        Material=Material,
        Notificacao=Notificacao,
        Pais=Pais,
        Pedido=Pedido,
        pedidos_itens = pedidos_itens,
        PontoDeVenda=PontoDeVenda,
        PrecoProduto=PrecoProduto,
        Producao=Producao,
        Produto=Produto,
        Usuario=Usuario,
        Unidade=Unidade,
        TipoPontoDeVenda=TipoPontoDeVenda,
        migrate=migrate,
        reinicializar=reinicializar
    )
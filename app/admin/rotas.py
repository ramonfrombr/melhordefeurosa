


















@app.route('/painel/pedido/<int:pedido_id>')
def pedido(pedido_id):

    pedido = Pedido.query.filter_by(
        id=pedido_id
        ).first_or_404()

    return render_template(
        'painel/pedido.html',
        pedido=pedido
    )


@app.route('/painel/entrega/<int:entrega_id>')
def entrega(entrega_id):

    entrega = Entrega.query.filter_by(
        id=entrega_id
        ).first_or_404()

    return render_template(
        'painel/entrega.html',
        entrega=entrega
    )


@app.route('/painel/unidade/<int:unidade_id>')
def unidade(unidade_id):
    
    unidade = Unidade.query.filter_by(
        id=unidade_id
        ).first_or_404()

    return render_template(
        '/painel/unidade.html',
        unidade=unidade
    )



@app.route('/painel/unidade/<int:unidade_id>/pedidos')
def pedidos_da_unidade(unidade_id):

    unidade = Unidade.query.filter_by(id=unidade_id).first_or_404()

    pedidos = unidade.pedidos.order_by(
        Pedido.data_registro.desc()
        ).all()

    return render_template(
        'painel/unidade/pedidos.html',
        unidade=unidade,
        pedidos=pedidos
    )


@app.route('/painel/unidade/<int:unidade_id>/entregas')
def entregas_da_unidade(unidade_id):
    return 1


@app.route('/painel/unidade/<int:unidade_id>/pontos_de_venda')
def pontos_de_venda_da_unidade(unidade_id):
    return 1


@app.route('/painel/unidade/<int:unidade_id>/funcionarios')
def funcionarios_da_unidade(unidade_id):
    return 1


@app.route('/painel/unidade/<int:unidade_id>/entregadores')
def entregadores_da_unidade(unidade_id):
    return 1


@app.route('/painel/ponto_de_venda/<int:ponto_venda_id>')
def ponto_de_venda(ponto_venda_id):
    return 1

@app.route('/painel/ponto_de_venda/<int:ponto_venda_id>/')
def pedidos_do_ponto_de_venda(ponto_venda_id):

    ponto_de_venda = PontoDeVenda.query.filter_by(id=ponto_venda_id).first_or_404()

    pedidos = ponto_de_venda.pedidos.order_by(Pedido.data_registro.desc()).all()

    return render_template(
        'painel/ponto_de_venda/pedidos',
        ponto_de_venda=ponto_de_venda,
        pedidos=pedidos
    )


@app.route('/painel/ponto_de_venda/<int:ponto_venda_id>/funcionarios')
def funcionarios_do_ponto_de_venda(ponto_venda_id):
    return 1
































# Lista de Unidades


# Lista das Unidades com mais Entregas


# Lista das Unidades com mais Pedidos


# Lista das Unidades que geram mais Receita


# Lista das Unidades com mais Encomendas





# Lista de Pontos de Venda


# Lista de Pontos de Venda por Unidade


# Lista dos Pontos de Venda com mais Pedidos


# Lista dos Pontos de Venda que geram mais Receita








# Lista dos Vendedores Externos


# Lista dos Vendedores Externos por Unidade


# Lista dos Vendedores Externos com mais Pedidos


# Lista dos Vendedores Externos que geram mais Receita






# Lista dos Entregadores


# Lista dos Entregadores por Unidade


# Lista dos Entregadores que fazem mais Entregas







# Lista dos Produtos


# Lista dos Produtos com mais Pedidos


# Lista dos Produtos com mais de uma unidade no mesmo pedido


# Lista dos Produtos com mais Entregas















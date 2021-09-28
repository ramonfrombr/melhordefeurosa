from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO

db = SQLAlchemy()
migrate = Migrate()
socketio = SocketIO()




def pagina_nao_encontrada(error):
    return render_template('404.html'), 404


def criar_app(configuracao):

    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/
    Arguments:
        object_name: the python path of the config object,
                     e.g. project.config.ProdConfig
    """

    # IMPORTANDO BLUEPRINTS
    from .painel.rotas import painel_blueprint, ExibirUsuarios, ExibirUnidades, ExibirProdutos, ExibirPedidos
    
    #from .admin import admin


    # FLASKAPP
    app = Flask(__name__)
    app.config.from_object(configuracao)


    # DEPENDÊNCIAS
    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)

    # REGISTRANDO BLUEPRINTS
    app.register_blueprint(painel_blueprint)
    #app.register_blueprint(blog_blueprint)



    # REGISTRANDO PLUGGABLE VIEWS
    app.add_url_rule('/usuarios', view_func=ExibirUsuarios.as_view('exibir_usuarios'))
    app.add_url_rule('/unidades', view_func=ExibirUnidades.as_view('exibir_unidades'))
    app.add_url_rule('/produtos', view_func=ExibirProdutos.as_view('exibir_produtos'))
    #app.add_url_rule('/painel/pedidos', view_func=ExibirPedidos.as_view('exibir_pedidos'))


    app.register_error_handler(404, pagina_nao_encontrada)


    
    return app
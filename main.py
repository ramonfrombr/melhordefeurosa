import os
from app import criar_app, socketio
from config import ConfiguracaoDesenvolvimento


#env = os.environ.get('WEBAPP_ENV', 'dev')
#app = criar_app('config.%sConfig' % env.capitalize())


app = criar_app(ConfiguracaoDesenvolvimento)

if __name__ == '__main__':
    socketio.run(app)
    #app.run()
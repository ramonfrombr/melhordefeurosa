from flask import Flask
from config import ConfiguracaoDesenvolvimento


app = Flask(__name__)
app.config.from_object(ConfiguracaoDesenvolvimento())


@app.route('/')
def inicio():
    return "Olá, mundo!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
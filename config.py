import os


class Configuracao(object):
    pass

class ConfiguracaoProducao(Configuracao):
    pass

class ConfiguracaoDesenvolvimento(Configuracao):
    ENV = True

    DEBUG = True

    SECRET_KEY = 'gjr39dkjn344_!67#'

    # Exibe um relatório dos comandos do SQL
    SQLALCHEMY_ECHO = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


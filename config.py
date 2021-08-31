class Configuracao(object):
    pass

class ConfiguracaoProducao(Configuracao):
    pass

class ConfiguracaoDesenvolvimento(Configuracao):
    ENV = True
    DEBUG = True


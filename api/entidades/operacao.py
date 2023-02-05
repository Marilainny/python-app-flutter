class Operacao():
    def __init__(self, nome, resumo, custo, tipo, conta):
        self.__nome = nome
        self.__resumo = resumo
        self.__custo = custo
        self.__tipo = tipo
        self.__conta = conta

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def resumo(self):
        return self.__resumo

    @resumo.setter
    def resumo(self, resumo):
        self.__resumo = resumo

    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, custo):
        self.__custo = custo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, conta):
        self.__conta = conta

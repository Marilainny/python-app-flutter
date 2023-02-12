"""
Classes com atributos, get e sets que será validado na class Schema
"""
class Conta():
    # construtor
    def __init__(self, nome, resumo, valor, usuario):
        self.__nome = nome
        self.__resumo = resumo
        self.__valor = valor
        self.__usuario = usuario #relacionamento com usuário

    # Gets e Sets
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
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

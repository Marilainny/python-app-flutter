"""
Classes com atributos, get e sets que será validado na class Schema
"""
class Conta():
    # construtor
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    # Gets e Sets
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor


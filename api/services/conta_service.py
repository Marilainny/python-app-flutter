'''
Onde cria os serviços arquivos com métodos interagindo com as operações e metódos do CRUD,
orientação objetos com o banco de dados relacionais, usando o SQLAlchemy para insersão de dados sem SQL
'''

from api import db
from ..models import conta_model

def listar_contas():
    contas = conta_model.Conta.query.all()
    return contas

def listar_conta_id(id):
    conta = conta_model.Conta.query.filter_by(id=id).first()
    return conta

def atualizar_conta(conta, conta_nova):
    conta.nome = conta_nova.nome
    conta.resumo = conta_nova.resumo
    conta.valor = conta_nova.valor
    db.session.commit()
    return conta

def cadastrar_conta(conta):
    conta_db = conta_model.Conta(nome=conta.nome, resumo=conta.resumo, valor=conta.valor)
    db.session.add(conta_db)
    db.session.commit()
    return conta_db

def excluir_conta(conta):
    db.session.delete(conta)
    db.session.commit()
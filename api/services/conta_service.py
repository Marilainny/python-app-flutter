'''
Onde cria os serviços arquivos com métodos interagindo com as operações e metódos do CRUD,
orientação objetos com o banco de dados relacionais, usando o SQLAlchemy para insersão de dados sem SQL
'''

from api import db
from ..models import conta_model

def cadastrar_conta(conta):
    conta_db = conta_model.Conta(nome=conta.nome, resumo=conta.resumo, valor=conta.valor)
    db.session.add(conta_db)
    db.session.commit()
    return conta_db
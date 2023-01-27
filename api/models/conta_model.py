"""
1- importar o db,
2- Criar a classe, que estende de db Model do SQLAlchemy,
3- Script para gerar a tabela no banco de dados.
4- Importar biblibiotecas no __init__.py (db = SQLAlchemy(app))
"""

from api import db

class Conta(db.Model):
    __tablename__='conta' #nome da tabela, sem informação pega o nome da classe.

    #atributos da tabela
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    resumo = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)


from api import db
from ..models import operacao_model

def listar_operacoes():
    operacoes = operacao_model.Operacao.query.all()
    return operacoes

def cadastrar_operacao(operacao):
    operacao_db = operacao_model.Operacao(
        nome=operacao.nome,
        resumo=operacao.resumo,
        custo=operacao.custo,
        tipo=operacao.tipo
    )
    db.session.add(operacao_db)
    db.session.commit()
    return operacao_db

from api import db
from ..models import operacao_model

def listar_operacoes():
    operacoes = operacao_model.Operacao.query.all()
    return operacoes

def listar_operacao_id(id):
    operacao = operacao_model.Operacao.query.filter_by(id=id).first()
    return operacao

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

def atualizar_conta(operacao, operacao_nova):
    operacao.nome = operacao_nova.nome
    operacao.resumo = operacao_nova.resumo
    operacao.custo = operacao_nova.custo
    db.session.commit()
    return operacao

def excluir_operacao(operacao):
    db.session.delete(operacao)
    db.session.commit()
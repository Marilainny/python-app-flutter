from api import db
from ..models import operacao_model
from ..services import conta_service

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
        tipo=operacao.tipo,
        conta_id=operacao.conta #conta_id conforme no model
    )
    db.session.add(operacao_db)
    db.session.commit()
    conta_service.alterar_saldo_conta(operacao.conta, operacao, 1)
    return operacao_db

def atualizar_operacao(operacao, operacao_nova):
    # para atualizar o valor operacão antes da atualização abaixo.
    valor_antigo = operacao.custo

    operacao.nome = operacao_nova.nome
    operacao.resumo = operacao_nova.resumo
    operacao.custo = operacao_nova.custo
    operacao.tipo = operacao_nova.tipo
    operacao.conta = operacao_nova.conta #conta conforme na entidade
    db.session.commit()

    conta_service.alterar_saldo_conta(operacao_nova.conta, operacao_nova, 2, valor_antigo)
    return operacao

def excluir_operacao(operacao):
    db.session.delete(operacao)
    db.session.commit()
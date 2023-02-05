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

def cadastrar_conta(conta):
    conta_db = conta_model.Conta(nome=conta.nome, resumo=conta.resumo, valor=conta.valor)
    db.session.add(conta_db)
    db.session.commit()
    return conta_db

def atualizar_conta(conta, conta_nova):
    conta.nome = conta_nova.nome
    conta.resumo = conta_nova.resumo
    conta.valor = conta_nova.valor
    db.session.commit()
    return conta

def excluir_conta(conta):
    db.session.delete(conta)
    db.session.commit()

def alterar_saldo_conta(conta_id, operacao, tipo_funcao, valor_antigo=None):
    conta = listar_conta_id(conta_id)
    #tipo_funcao -> 1 = Cadastro de Operação
    if tipo_funcao == 1:
        if operacao.tipo =='entrada':
            conta.valor += operacao.custo
        else:
            conta.valor -= operacao.custo
    # tipo_funcao -> 2 = Atualização de Operação
    elif tipo_funcao == 2:
        if operacao.tipo == 'entrada':
            conta.valor -= valor_antigo
            conta.valor += operacao.custo
        else:
            # tipo_funcao -> 3 = Remoção de Operação
            conta.valor += valor_antigo
            conta.valor -= operacao.custo

    db.session.commit()
"""
Define as rotas e implementação recurso API, métodos como no HTTP
"""
from flask_restful import Resource
from ..schemas import conta_schema
from flask import request, make_response, jsonify
from ..entidades import conta
from ..services import conta_service
from api import api


class ContaList(Resource):  # A classe é um recurso

    def get(self):
        contas = conta_service.listar_contas()
        cs = conta_schema.ContaSchema(many=True) # select tabela contas
        return make_response(cs.jsonify(contas), 201)
    def post(self):
        cs = conta_schema.ContaSchema()  # validação
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)  # resposta em json do servidor
        else:  # recuperar as informações
            nome = request.json["nome"]
            resumo = request.json["resumo"]
            valor = request.json["valor"]
            conta_nova = conta.Conta(nome=nome, resumo=resumo, valor=valor)  # dados para construtor
            resultado = conta_service.cadastrar_conta(conta_nova)  # cadastrar a conta
            return make_response(cs.jsonify(resultado), 201)
class ContaDetail(Resource):
    def get(self, id):
        conta = conta_service.listar_conta_id(id)
        if conta is None:
            return make_response(jsonify("Conta não encontrada"), 404)
        cs = conta_schema.ContaSchema()
        return make_response(cs.jsonify(conta), 200)
    def put(self, id):
        conta_bd = conta_service.listar_conta_id(id)
        if conta is None:
            return make_response(jsonify("Conta não encontrada"), 404)
        cs = conta_schema.ContaSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            resumo = request.json["resumo"]
            valor = request.json["valor"]
            conta_nova = conta.Conta(nome=nome, resumo=resumo, valor=valor)
            resultado = conta_service.atualizar_conta(conta_bd, conta_nova)
            return make_response(cs.jsonify(resultado), 201)

    def delete(self, id):
        conta = conta_service.listar_conta_id(id)
        if conta is None:
            return make_response(jsonify("Conta não encontrada"), 404)
        conta_service.excluir_conta(conta)
        make_response(jsonify(""), 204)

# rota de acesso
api.add_resource(ContaList, '/contas')
api.add_resource(ContaDetail, '/contas/<int:id>')

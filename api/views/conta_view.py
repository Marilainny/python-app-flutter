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


# rota de acesso
api.add_resource(ContaList, '/contas')

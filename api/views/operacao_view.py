from flask import request, make_response, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from api import api
from ..entidades import operacao
from ..schemas import operacao_schema
from ..services import operacao_service, conta_service
from ..decorators.autorizacao import user_operacao

class OperacaoList(Resource):

    @jwt_required()
    def get(self):
        usuario_logado = get_jwt_identity()
        operacoes = operacao_service.listar_operacoes(usuario_logado)
        os = operacao_schema.OperacaoSchema(many=True)
        return make_response(os.jsonify(operacoes), 201)

    @jwt_required()
    def post(self):
        os = operacao_schema.OperacaoSchema()
        validate = os.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            resumo = request.json["resumo"]
            custo = request.json["custo"]
            tipo = request.json["tipo"]
            conta = request.json["conta_id"] # conta_id conforme no model.

            if conta_service.listar_conta_id(conta) is None:
                return make_response("Conta não existe", 404)
            else:
                operacao_nova = operacao.Operacao(
                    nome=nome,
                    resumo=resumo,
                    custo=custo,
                    tipo=tipo,
                    conta=conta # conta conforme na entidade
                )
            resultado = operacao_service.cadastrar_operacao(operacao_nova)
            return make_response(os.jsonify(resultado), 201)

class OperacaoDetail(Resource):
    @user_operacao
    def get(self, id):
        operacao = operacao_service.listar_operacao_id(id)
        if operacao is None:
            return make_response(jsonify("Operação não encontrada"), 404)
        os = operacao_schema.OperacaoSchema()
        return make_response(os.jsonify(operacao), 200)

    @user_operacao
    def put(self, id):
        operacao_bd = operacao_service.listar_operacao_id(id)
        if operacao is None:
            return make_response(jsonify("Conta não encontrada"), 404)
        os = operacao_schema.OperacaoSchema()
        validate = os.validate( request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            resumo = request.json["resumo"]
            custo = request.json["custo"]
            tipo = request.json["tipo"]
            conta = request.json["conta_id"]  # conta_id conforme no model.

            if conta_service.listar_conta_id(conta) is None:
                return make_response("Conta não existe", 404)
            else:
                operacao_nova = operacao.Operacao(
                    nome=nome,
                    resumo=resumo,
                    custo=custo,
                    tipo=tipo,
                    conta=conta
                )
            resultado = operacao_service.atualizar_operacao(operacao_bd, operacao_nova)
            return make_response(os.jsonify(resultado), 201)

    @user_operacao
    def delete(self, id):
        operacao = operacao_service.listar_operacao_id(id)
        if operacao is None:
            return make_response(jsonify("Conta não encontrada"), 404)
        operacao_service.excluir_operacao(operacao)
        make_response(jsonify(""), 204)


api.add_resource(OperacaoList, '/operacoes')
api.add_resource(OperacaoDetail, '/operacoes/<int:id>')
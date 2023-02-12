from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from ..services import conta_service, operacao_service
from flask import make_response, jsonify

def user_conta(view_function):
    @wraps(view_function)
    def decorator_funtion(*args, **kwargs):
        verify_jwt_in_request() #verificar se existe uma chave token
        usuario_logado = get_jwt_identity()
        conta = conta_service.listar_conta_id(kwargs['id'])
        if conta is None:
            return make_response(jsonify("Conta não existe"), 404)
        elif conta.usuario_id == usuario_logado:
            return view_function(*args, **kwargs)
        else:
            return make_response(jsonify("Esta conta não pertence ao usuário logado"), 403)
    return decorator_funtion

def user_operacao(view_function):
    @wraps(view_function)
    def decorator_funtion(*args, **kwargs):
        verify_jwt_in_request()
        usuario_logado = get_jwt_identity()
        operacao = operacao_service.listar_operacao_id(kwargs['id'])
        if operacao is None:
            return make_response(jsonify("Operação não encontrada"), 404)
        else:
            conta = conta_service.listar_conta_id(operacao.conta_id)
            if conta.usuario_id == usuario_logado:
                return view_function(*args, **kwargs)
            else:
                return make_response ( jsonify ( "Esta operação não pertence ao usuário logado" ), 403 )
    return decorator_funtion
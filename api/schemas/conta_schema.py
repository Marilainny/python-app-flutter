"""
validação de dados, validar as regras de negócio, conversões como jason, texto, precisa das bibliotecas Marshmallow
precisa importar biblibiotecas no __init__.py (ma = Marshmallow(app)).
"""

from api import ma
from ..models import conta_model
from marshmallow import fields

class ContaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = conta_model.Conta
        load_instance = True

        nome = fields.String(required=True)
        resumo = fields.String(required=True)
        valor = fields.Float(required=True)
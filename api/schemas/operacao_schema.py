from marshmallow import fields
from marshmallow_enum import EnumField

from api import ma
from ..models import operacao_model


class OperacaoSchema(ma.SQLAlchemyAutoSchema):
    tipo = EnumField(operacao_model.TipoEnum)
    class Meta:
        model = operacao_model.Operacao
        load_instance = True

        nome = fields.String(required=True)
        resumo = fields.String(required=True)
        custo = fields.Float(required=True)

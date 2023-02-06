"""
validação de dados, validar as regras de negócio, conversões como jason, texto, precisa das bibliotecas Marshmallow
precisa importar biblibiotecas no __init__.py (ma = Marshmallow(app)).
"""

from api import ma
from ..models import usuario_model
from marshmallow import fields

class UsuarioSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = usuario_model.Usuario
        load_instance = True

        nome = fields.String(required=True)
        email = fields.String(required=True)
        senha = fields.String(required=True)
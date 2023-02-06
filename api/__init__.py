'''
configuração de inicialização da API, referente as blibiotecas da aplicação.
Tem as importações das blibiotecas, nome do aplicativo, objetos buscando as configurações do banco de dados,
informações do banco de dados, a migração, importação do models.
Cada pacote deve ser adicionado no projeto deve ser importado neste arquivo de inicialização.
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

ma = Marshmallow(app)

mi = Migrate(app, db)

api = Api(app)

#informar model antes de rodar o migrate
from .models import conta_model, operacao_model, usuario_model
from .views import conta_view, operacao_view, usuario_view

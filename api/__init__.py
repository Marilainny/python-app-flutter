'''
Configuração de inicialização da API, referente as blibiotecas da aplicação.
Tem as importações das blibiotecas, nome do aplicativo, objetos referência as configurações do banco de dados,
informações do banco de dados, a migração, importação do models.
Cada pacote deve ser adicionado no projeto deve ser importado neste arquivo de inicialização.
'''

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

ma = Marshmallow(app)

db = SQLAlchemy(app)

mi = Migrate(app, db)

api = Api(app)

#from .models import conta_model, operacao_model
#from .views import conta_view, operacao_view
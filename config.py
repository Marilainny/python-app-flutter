''' INFORMAÇÕES DO BANCO DE DADOS'''

DEBUG = True #permite fazer alterações sem a necessidade de parar o servidor

USERNAME = 'root'
PASSWORD = 'mms4525'
SERVER = 'localhost'
DB = 'gerenciamento_contas'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'

#atualizar migrações
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'chave_secreta1'
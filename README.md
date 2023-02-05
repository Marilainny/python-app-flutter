CONFIGURAÇÃO AMBIENTE

1- instalar o python
2- pip install Flask (Precisa ter o Python instalado para intalar o Flask)
3- dart --version (Instalar o Flutter C:\bin)
4- flutter --version

Dart SDK version: 2.18.6
Dart SDK version: 2.18.6
Python 3.10.4 

5 - BIBLIOTECAS

Flask
SQLAlchemy
Flask-SQLAlchemy
mysqlclient
Flask-Migrate
Marshmallow
Flask-marshmallow
marshmallow-sqlalchemy
marshmallow-enum
Flask-Restful

6- CRIAR BANCO DE DADOS MYSQL (gerenciamento_conta)

mysql -u root -p
create database gerenciamento_conta;
show databases;
use gerenciamento_contas;
show tables;
desc conta;
drop table nome_tabela;

7- SERVIDOR FLASK

C:\caminho_projeto\gerenciamento_contas\venv\Scripts\activate
cd C:\caminho_projeto\gerenciamento_contas\
set FLASK_APP=api

8- ARQUIVOS RAIZ:

config - informações do banco de dados

arquivo - run para rodar o projeto

7- ESTRUTURA DIRETÓRIOS

entidades: classes com atributos, get e sets mesmos atributos de model e o metódo inicial

models: base central, arquivos criar e especificar os atributos das tabelas, tipos de dados, chave primaria relacionada.

schemas: validação de dados, validar as regras de negócio, conversões como jason, texto.

service: onde cria os serviços arquivos com métodos interagindo com as operações e metódos,  orientação objetos com o banco de dados relacionais

views: define as rotas e implementação recurso API. 

ESTRUTURA

PACKAGE - api
ARQUIVO - __init__.py
DIRETORIOS - entidades, models, schemas, services, views
ARQUIVO RAIZ - config.py

8 - SERVIDRO FLASK

Comandos no Terminal

SEU PROJETO\venv\Scripts\activate
SEU PROJETO\

set FLASK_APP=api
flask run 
flask db init
flask db migrate
flask db upgrade






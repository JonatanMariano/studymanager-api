# StudyManager API

API RESTful desenvolvida com FastAPI e SQLAlchemy para gerenciamento de usuários, cursos e matrículas.

## Tecnologias

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Estrutura do Projeto

controllers → recebem requisições HTTP  
services → regras de negócio  
repositories → acesso ao banco de dados  
models → entidades ORM  
schemas → validação de dados

A arquitetura segue princípios de Arquitetura Limpa, separando responsabilidades em camadas para facilitar manutenção, testes e escalabilidade.

## Executar projeto

pip install -r requirements.txt

uvicorn app.main:app --reload --port 8001

## Documentação

http://127.0.0.1:8001/docs

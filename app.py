from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel

from tinydb import TinyDB

server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='Live de Python')
spec.register(server)
database = 


class Pessoa(BaseModel):
    id: int
    nome: str
    idade: int 

@server.get('/')
@spec.validate(resp=Response(HTTP_200=Pessoa))
def pegar_pessoas():
    return 'Victor soares'

server.post('/')
@spec.validate(body=Pessoa, resp=Pessoa(HTTP_200=Pessoa))
def inserir_pessoa():
    body = request.context.body.dict()
    return body
    
    

if __name__ == "__main__":
    server.run()
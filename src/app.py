from flask import Flask, request
from flask.wrappers import Response
from bson import json_util
from pymongo import database
from .Models.user import User
from .persistence.database.db import Database

app = Flask(__name__)

connectionDb = Database() # Create the connectio with db

@app.route('/user/', methods=['GET'])
def getAllUsers():
    try:
        data_users = connectionDb.find_all_users()
        response = json_util.dumps(data_users)
    except:
        response = {"code": 500,
                    "error": "Ocorreu um erro interno no servidor."}
        response = json_util.dumps(response)
        return Response(response, status=500)
    return Response(response, status=200)

@app.route('/user/', methods=['POST'])
def index():
    request_data = request.get_json()
    first_name = request_data['first_name']
    last_name = request_data['last_name']
    login = request_data['login']
    plaintext_password = request_data["plaintext_password"]


    if first_name and last_name and login and plaintext_password:
        user = User(first_name,last_name,login,plaintext_password)
        User.hash_password(plaintext_password) # Encrypting the password
        if user.validate_password(plaintext_password): # if validatation is true change for new password and insert in database
            request_data['plaintext_password'] = User.password
            user._id = connectionDb.insert(request_data)
            response = {"code": 200,
                        "_id": user._id}
            response = json_util.dumps(response)
            return Response(response, status=200) 
    else:
        response = {"code": 400,
                    "error": "Pedido invalido verifique seus dados."}
        response = json_util.dumps(response)
        return Response(response, status=400)

   

        #user = User(request_data[])

    #O ID do usuário deverá ser gerado pelo servidor, e não passado pela requisição.

    #Cria um usuário com os dados passados.
    #  A requisição será realizada em JSON, com os seguintes dados no corpo:

    #O campo plaintext_password deverá ser convertido para o atributo password do modelo User utilizando o método hash_password
    #O retorno deverá ser com código HTTP 200, com um JSON indicando o ID do usuário que foi criado. Ex: {"_id": "123456abc"}.
    return None


@app.route('/user/<id>/', methods=['GET'])
def getUserForId(id):
    try:
        data_user = connectionDb.find_user(id)
    except:
        response = {"code": 500,
                    "error": "Ocorreu um erro interno no servidor."}
        response = json_util.dumps(response)
        return Response(response, status=500)
    else:
        if data_user is None:
            response = { "code": 404,
                         "error": "user not found"}
            response = json_util.dumps(response)
            return Response(response, status=404)
        else:
            response = json_util.dumps(data_user)
            return Response(response, status=200)

@app.route('/user/<id>/', methods=['PUT'])
def put(id):    
    
    #Atualiza os dados de um usuário já criado, filtrado pelo id passado na URL.
    #Se o usuário não existir, retornar o código HTTP 404, com uma mensagem em JSON com: {"error": "user not found"}.
    #A requisição será realizada em JSON, com os seguintes dados no corpo:
    return None

@app.route('/user/<id>/', methods=['DELETE'])
def delete(id):   
    try:
        print("Deletando...")
        data = connectionDb.delete_user(id)
    except Exception as ex:
        print(ex)
        response = {"code": 500,
                    "error": "Ocorreu um erro interno no servidor."}
        response = json_util.dumps(response)
        return Response(response, status=500)
    else:
        if data is None:
            response = { "code": 404,
                         "error": "user not found"}
            response = json_util.dumps(response)
            return Response(response, status=404)
        else:
            response = {"code": 204,
                        "message": "Operation performed successfully. There is no data to be returned."}
            response = json_util.dumps(response)
            return Response(response, status=204)


  #  Deleta um usuário criado, filtrado pelo id passado na URL.
  #      Se o usuário não existir, retornar o código HTTP 404, com uma mensagem em 
  #      JSON com: {"error": "user not found"}.
    return None

@app.route('/login/', methods=['POST'])
def post(id):  
    """ A requisição será realizada em JSON, com os seguintes dados no corpo:
    O campo password receberá uma senha em plaintext, que será validada a partir do usuário que possui o login correspondente pelo método validate_password.
    Caso não exista nenhum usuário com o login fornecido, retorne um 404 com o json: {"error": "user not found"}.
    Caso o usuário exista, mas a senha não esteja correta, retorne um HTTP 401 com o json: {"error": "invalid password"}
    Caso o usuário exista e senha seja válida, retorne um JSON com um token aleatório (hash). Ex: {"token": "12345689abceef"}"""
    return None



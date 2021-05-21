import random
from flask import Flask, request
from flask.wrappers import Response
from bson import json_util
from .Models.user import User
from .persistence.database.db import Database
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/v1/reference'
API_URL = '/static/swagger.yaml'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Crud of users"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

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
def postDataUser():
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
    else:
        response = {"code": 400,
                    "error": "Pedido invalido verifique seus dados."}
        response = json_util.dumps(response)
        return Response(response, status=400)


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
    verifyUser = connectionDb.find_user(id)
    if verifyUser is None:
        response = { "code": 404,
                     "error": "user not found"}
        response = json_util.dumps(response)
        return Response(response, status=404)
    else:
        request_data = request.get_json()
        first_name = request_data['first_name']
        last_name = request_data['last_name']
        login = request_data['login']
        plaintext_password = request_data["plaintext_password"]

        if first_name and last_name and login and plaintext_password:
            user = User(first_name,last_name,login,plaintext_password)
            user._id = id
            User.hash_password(plaintext_password) # Encrypting the password
            if user.validate_password(plaintext_password): # if validatation is true change for new password and insert in database
                request_data['plaintext_password'] = User.password
                dataUpdated = connectionDb.update_user(id,request_data)
                response = {"code": 200,
                            "message": "Sucesso in the operation."}
                response = json_util.dumps(response)
                return Response(response, status=200) 
            else:
                response = {"code": 400,
                        "error": "Pedido invalido verifique seus dados."}
                response = json_util.dumps(response)
                return Response(response, status=400)
        else:
            response = {"code": 400,
                        "error": "Pedido invalido verifique seus dados."}
            response = json_util.dumps(response)
            return Response(response, status=400)


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


@app.route('/login/', methods=['POST'])
def post():  
    request_data = request.get_json()
    login = request_data['login']
    password = request_data["password"]

    verifyUser = connectionDb.find_login(login)

    if verifyUser is None:
        response = { "code": 404,
                     "error": "user not found"}
        response = json_util.dumps(response)
        return Response(response, status=404)
    else:
        user = User(verifyUser["first_name"], verifyUser["last_name"], verifyUser["login"], verifyUser["plaintext_password"])
        user._id = verifyUser['_id']
        User.password = verifyUser["plaintext_password"]
        if user.validate_password(password):
            token_random = random.getrandbits(128)
            response = {"code": 200,
                        "token": token_random}
            response = json_util.dumps(response)
            return Response(response, status=200)
        else:
            response = {"code": 401,
                        "error": "Invalid password"}
            response = json_util.dumps(response)
            return Response(response, status=400)
        



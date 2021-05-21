import re
from pymongo import MongoClient
from bson.json_util import ObjectId

class Database:
    name_collection='Datas'
    connection = None
    def __init__(self):
        self.set_connection()

    def set_connection(self):
        try:
            client_connection = MongoClient("mongodb://127.0.0.1:27017/")
            db = client_connection['Users']
            self.connection = db[self.name_collection]
        except Exception as ex:
            raise ex
        else:
             print("Connection created.")
    
    def insert(self, documento_user: dict):
        try:
            response = self.connection.insert_one(documento_user)
        except Exception as ex:
            raise ex
        else:
            return str(response.inserted_id)

    def update_user(self,user_id,newDocumento):
        try:
            response = self.connection.find_one_and_update(
                {'_id': ObjectId(user_id)},
                 {'$set': newDocumento},
                return_document=True)
        except Exception as ex:
            raise ex
        else:
            if response is None:
                raise Exception('Unexpected value.')
            else:
                return response
    
    def find_user(self,user_id):
        try:
            response = self.connection.find_one({'_id': ObjectId(user_id)})
        except Exception as ex:
            raise ex
        else:
            return response

    def find_all_users(self):
        try:
            response = self.connection.find()
        except Exception as ex:
            raise ex
        else:
            if response is not None:
                return list(response)
            else:
                print("There is no data in the database.")
                return response

    def find_login(self, login, password):
        try:
            response = self.connection.find_one({'login': login, 'senha': password}) 
        except Exception as ex:
            raise ex
        else:
            return response

    def delete_user(self, user_id):
        try:
            response = self.connection.find_one_and_delete({'_id': ObjectId(user_id)})
            print("TO AQ")
            print(response)
        except Exception as ex:
            print(ex)
            raise ex
        return user_id

       
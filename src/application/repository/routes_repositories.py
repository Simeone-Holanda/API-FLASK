from bson.json_util import ObjectId
from ...util.dataFormatter import remove_objectId,remove_objectIdInArray
from ...persistence.schemas.schema import schema_json
from ...background import ServiceBackground
from pymongo.errors import CollectionInvalid ,WriteError 
from collections import OrderedDict

class Repository:
    instanceBd = None
    def __init__(self):
        self.instanceBd = ServiceBackground.getConnectionDb()
        try:
            #self.instanceBd.create_collection('Datas')
            self.__define_collection('Datas')
        except CollectionInvalid:
            pass
        

    def insert_user(self, documento_user: dict):
        try:
            response = self.instanceBd['Datas'].insert_one(documento_user)
        except WriteError as ex:
            print(ex)
            raise ex
        else:
            return str(response.inserted_id)

    def update_user(self,user_id,newDocumento):
        try:
            response = self.instanceBd['Datas'].find_one_and_update(
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
            response = self.instanceBd['Datas'].find_one({'_id': ObjectId(user_id)})
            if response is None:
                return response
            newResponse = remove_objectId(response)
        except Exception as ex:
            print(ex)
            raise ex
        else:
            return newResponse

    def find_all_users(self):
        try:
            response = list(self.instanceBd['Datas'].find())
            response = remove_objectIdInArray(response)
        except Exception as ex:
            print(ex)
            raise ex
        else:
            if response is not None:
                return response
            else:
                print("There is no data in the database.")
                return response

    def find_login(self, login):
        try:
            response = self.instanceBd['Datas'].find_one({'login': login}) 
            newResponse = remove_objectId(response)
        except Exception as ex:
            print(ex)
            raise ex
        else:
            return newResponse

    def delete_user(self, user_id):
        try:
            response = self.instanceBd['Datas'].find_one_and_delete({'_id': ObjectId(user_id)})
            print(response)
        except Exception as ex:
            print(ex)
            raise ex
        return response

    def __define_collection(self,nameCollection):
        try:
            self.instanceBd.create_collection(nameCollection)
            analises_schema = schema_json()
            dados = [('collMod', nameCollection), ('validator', analises_schema),
                        ('validationLevel', 'moderate')]
            self.instanceBd.command(OrderedDict(dados))
        except CollectionInvalid as ex:
            pass 
        except Exception as ex:
            print(ex)

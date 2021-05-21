from bson.json_util import ObjectId

from ...background import ServiceBackground

class Repository:
    instanceBd = None
    def __init__(self):
        self.instanceBd = ServiceBackground.getConnectionDb()['Datas']

    def insert(self, documento_user: dict):
        try:
            response = self.instanceBd.insert_one(documento_user)
        except Exception as ex:
            raise ex
        else:
            return str(response.inserted_id)

    def update_user(self,user_id,newDocumento):
        try:
            response = self.instanceBd.find_one_and_update(
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
            response = self.instanceBd.find_one({'_id': ObjectId(user_id)})
        except Exception as ex:
            raise ex
        else:
            return response

    def find_all_users(self):
        try:
            response = self.instanceBd.find()
        except Exception as ex:
            print(ex)
            raise ex
        else:
            if response is not None:
                return list(response)
            else:
                print("There is no data in the database.")
                return response

    def find_login(self, login):
        try:
            response = self.instanceBd.find_one({'login': login}) 
        except Exception as ex:
            raise ex
        else:
            return response

    def delete_user(self, user_id):
        try:
            response = self.instanceBd.find_one_and_delete({'_id': ObjectId(user_id)})
            print(response)
        except Exception as ex:
            print(ex)
            raise ex
        return response

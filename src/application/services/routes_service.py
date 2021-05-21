from ..repository.routes_repositories import Repository

class Services:
    connectionDb = None
    def __init__(self):
        self.connectionDb = Repository()
    
    def getAllUserService(self):
        try: 
            return self.connectionDb.find_all_users()
        except Exception:
            raise Exception("Error in the method getAllUserService.")

    def postDataUserService(self,datas: dict):
        try:
            return self.connectionDb.insert(datas)
        except Exception:
            raise Exception("Error in the method postDataUserService.")
    
    def getUserForIdService(self,id):
        try:
             return self.connectionDb.find_user(id)
        except Exception:
            raise Exception("Error in the method getUserForIdService.")

    def updateDateUserService(self,id, newDocument):
        try:
            return self.connectionDb.update_user(id,newDocument)
        except Exception:
            raise Exception("Error in the method updateDateUserService.")


    def deleteUserForIdService(self,id):
        try:
            return self.connectionDb.delete_user(id)
        except Exception as ex:
            raise Exception("Error in the method deleteUserForIdService.")

    def postLoginService(self,login):
        try:
            return self.connectionDb.find_login(login)
        except Exception:
            raise Exception("Error in the method postLoginService.")

    
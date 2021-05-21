from pymongo import MongoClient

class Database:    
    db = None

    @classmethod
    def set_connection(cls):
        """
        With this statistical method we apply the singleton pattern and prevent a connection 
        from being made more than once in the program.
        """
        try:
            print("===========creted connection=============")
            
            client_connection = MongoClient("mongodb://127.0.0.1:27017/")
            cls.db = client_connection['Users']
        except Exception as ex:
            raise ex

    @classmethod
    def get_connection(cls):
        """
        With this statistical method we will always have the connection that has already been made available.
        """
        print("==============Get connection=============")
        return cls.db

    
       
from .persistence.database import db

class ServiceBackground:

    def __init__(self):
        db.Database.set_connection()

    @staticmethod
    def getConnectionDb():
        return db.Database.get_connection()
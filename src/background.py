from .persistence.database import db_factory

class ServiceBackground:

    def __init__(self):
        """
        Without the database service, no operation is possible, so it must be checked 
        before starting the application.
        """
        db_factory.Database.set_connection()

    @staticmethod
    def getConnectionDb():
        return db_factory.Database.get_connection()
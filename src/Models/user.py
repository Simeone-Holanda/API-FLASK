from passlib.hash import bcrypt

class User:
    _id = None
    first_name = None
    last_name = None
    login = None
    password = None

    def __init__(self, first_name, last_name,login, password):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password

    @staticmethod
    def hash_password(plaintext_password:str):
        print("Dentro do hash")
        print(plaintext_password)
        hash = bcrypt.hash(plaintext_password)
        User.password = hash

    @staticmethod
    def validate_password(plaintext_password:str):
        print(plaintext_password)
        print(User.password)
        return bcrypt.verify(plaintext_password,User.password)
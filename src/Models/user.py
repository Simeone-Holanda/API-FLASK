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
        hash = bcrypt.hash(plaintext_password)
        User.password = hash

    @staticmethod
    def validate_password(plaintext_password:str):
        return bcrypt.verify(plaintext_password,User.password)

     # Metodo statico
    #Este método irá criar um hash do password do usuário, para não salvar 
    # o plaintext no banco. Utilizar o método bcrypt da biblioteca passlib.hash

    #validate_password(plaintext_password : string) -> bool - Metodo statico
    #Este método verifica se o password passado em plaintext é o gerador do hash que está presente no atributo self.password.
    #Retorna True se o password foi validado, ou False se não é o password gerador.
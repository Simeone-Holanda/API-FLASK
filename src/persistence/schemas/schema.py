
def schema_json():
    schema_bd = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["first_name","last_name","login","plaintext_password"],
            "properties": {
                "first_name": {
                    "bsonType": "string",
                    "description": "Type string requerid"
                },
                "last_name": {
                    "bsonType": "string",
                    "description": "Type string requerid"
                },
                "login": {
                    "bsonType": "string",
                    "description": "Type string requerid"
                },
                "plaintext_password": {
                    "bsonType": "string",
                    "description": "Type string requerid"
                }
            }
        }
    }
    return schema_bd
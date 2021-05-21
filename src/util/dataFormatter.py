
def remove_objectId(document: dict):
    try:
        print(document['_id'])
        id = str(document['_id'])
        document['_id'] = id
    except Exception as ex:
        print(ex)
        raise ex
    return document

def remove_objectIdInArray(document_list: list):
    for document in document_list:
        id = str(document['_id'])
        document['_id'] = id
    return document_list


def schema_json():
    schema_bd = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["user_id", "metrics"],
            "properties": {
                "user_id": {
                    "bsonType": "string",
                    "description": "Type string requerid"
                    },
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
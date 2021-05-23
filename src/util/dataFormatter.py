
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



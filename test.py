def remove_objectId(document: dict):
    id = str(document['_id']['$oid'])
    del document['_id']['$oid']
    document['_id'] = id
    return document

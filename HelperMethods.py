import json


def getFieldsFromString(s):
    split_s = s.split()
    id, name, email, customId, customName, customField1, customField2, customField3, externalId = split_s
    return id, name, email, customId, customName, customField1, customField2, customField3, externalId


def createDictionaries(id, name, email, customId, customName, customField1, customField2, customField3, externalId):
    d1 = {
        'id': id,
        'name': name,
        'email': email,
        'type': {
            'id': customId,
            'name': customName,
            'customFields': {
                'c1': customField1,
                'c2': customField3,
                'c3': customField3
            }
        },
        'externalId': externalId
    }

    d2 = {
        'email': email,
        'externalId': externalId,
        'id': id,
        'name': name,
        'type': {
            'customFields': {
                'c1': customField1,
                'c2': customField2,
                'c3': customField3
            },
            'id': id,
            'name': name
        }
    }

    return d1, d2


def createJsonOutput(d1, d2):
    with open("./sample.json", "w+") as outfile:
        json.dump([d1, d2], outfile)

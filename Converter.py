from HelperMethods import getFieldsFromString, createDictionaries, createJsonOutput
from pathlib import Path


def main():

    # replace this with your choice of string
    s = "13 Becky becky@gmail.com 13 Becky custom1 custom2 custom3 195"
    id, name, email, customId, customName, customField1, customField2, customField3, externalId = getFieldsFromString(
        s)

    d1, d2 = createDictionaries(id, name, email, customId, customName,
                                customField1, customField2, customField3, externalId)

    createJsonOutput(d1, d2)


main()

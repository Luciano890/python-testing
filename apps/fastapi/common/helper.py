""" This is a helper module for the FastAPI app. """

async def remove_id_field(document):
    """ Remove the _id field from the document. """
    document.pop("_id")
    return document

async def get_one_document(collection, query):
    """ Get one document from the collection. """
    return await collection.find_one(query)

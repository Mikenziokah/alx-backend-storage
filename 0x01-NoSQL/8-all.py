#!/usr/bin/python3
"""function that lists all documents in a collection
"""

import pymongo


def list_all(mongo_collection):
    """ listing all docs in a collection
    """
    docs = mongo_collection.find()
    return [i for i in docs]

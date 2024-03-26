#!/usr/bin/env python3
"""function that inserts a new document in
    a collection based on kwargs
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """ inserts docs based on kwargs
    """
    new_name = mongo_collection.insert_one(kwargs)
    return new_name.inserted_id

#!/usr/bin/env python3
""" function that changes all topics of a school
    document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """ changing school documents based on name
    """
    query = {"name": name}
    new_names = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_names)

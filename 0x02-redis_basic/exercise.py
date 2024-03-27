#!/usr/bin/env python3
""" creating a catche method to store an instance in redis
"""

import redis
from typing import union
from uuid import uuid4

class Cache:
    def __init__(self):
        """ the cache method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

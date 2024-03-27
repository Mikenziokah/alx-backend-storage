#!/usr/bin/env python3
""" creating a catche method to store an instance in redis
"""

import redis
from typing import Union, Callable
from uuid import uuid4
import uuid
import sys

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

    def decode_utf8(b: bytes) -> str:
        """ Decodes
        """
        return b.decode('utf-8') if type(b) == bytes else b


    def replay(method: Callable):
        """ Replay method
        """
    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])
    count = method.__self__.get(key)
    i_list = method.__self__._redis.lrange(i, 0, -1)
    o_list = method.__self__._redis.lrange(o, 0, -1)
    queue = list(zip(i_list, o_list))
    print(f"{key} was called {decode_utf8(count)} times:")
    for k, v, in queue:
        k = decode_utf8(k)
        v = decode_utf8(v)
        print(f"{key}(*{k}) -> {v}")
#!/usr/bin/env python3
"""MRU Caching"""

from base_caching import BaseCaching
from collections import OrderedDict

class MRUCache(BaseCaching):
    """A cache system that implements MRU caching"""

    def __init__(self):
        """
        Initialize the class
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = next(iter(self.cache_data))
            del self.cache_data[discarded]
            print("DISCARD:", discarded)
            
    def get(self, key):
        """
        Retrieve an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None

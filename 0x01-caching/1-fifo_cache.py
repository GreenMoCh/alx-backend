#!/usr/bin/env python3
""" FIFO caching """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A cache system that implements FIFO caching"""

    def __init__(self):
        """
        Initializes the class
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key not in self.keys:
            self.keys.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = self.keys.pop(0)
            del self.cache_data[discarded]
            print("DISCARD:", discarded)

    def get(self, key):
        """
        Retrieve an item by key
        """
        return self.cache_data.get(key, None)
        
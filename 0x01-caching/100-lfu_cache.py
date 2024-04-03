#!/usr/bin/env python3
"""LFU Caching"""

from base_caching import BaseCaching


class  LFUCaching(BaseCaching):
    """A caching system using LFU caching"""

    def __init__(self):
        """
        Initializes the class
        """
        super().__init__()
        self.cache_data = {}
        self.usage_counts = {}
        self.last_used = {}
        self.time = 0

    def put(self, key, item):
        """
        Assign item value for the key in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.usage_counts[key] = self.usage_counts.get(key, 0) + 1
        self.time += 1
        self.last_used[key] = self.time

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_freq = sorted(
                self.cache_data.keys()
                key=lambda k: (self.usage_counts[k], self.last_used[k])
            )[0]
            del self.cache_data[least_freq]
            del self.usage_counts[least_freq]
            del self.last_used[least_freq]
            print("DISCARD: {}".format(least_freq))

    def get(self, key):
        """
        Return the value linked to key
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_counts[key] += 1
        self.time += 1
        self.last_used[key] = self.time

        return self.cache_data[key]
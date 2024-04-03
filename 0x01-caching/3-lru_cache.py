#!/usr/bin/python3
"""
LRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    An instance of LRUCache class that inherits from the
    BaseCaching class
    """
    def __init__(self):
        """Instantiates an instance of the LRUCache class"""
        super().__init__()
        self.history = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if self.cache_data.get(key):
            self.history.remove(key)
        self.history.append(key)
        self.cache_data[key] = item
        if len(self.history) > self.MAX_ITEMS:
            srt = self.history.pop(0)
            print('DISCARD {}'.format(srt))
            self.cache_data.pop(srt)

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None
        if self.cache_data.get(key):
            self.history.remove(key)
            self.history.append(key)
            return self.cache_data.get(key)

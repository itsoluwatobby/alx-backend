#!/usr/bin/python3
"""
MRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    An instance of MRUCache class that inherits from the
    BaseCaching class
    """
    def __init__(self):
        """Instantiates an instance of the MRUCache class"""
        super().__init__()
        self.history = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if self.cache_data.get(key):
            self.history.remove(key)
        while len(self.history) >= self.MAX_ITEMS:
            srt = self.history.pop()
            print('DISCARD {}'.format(srt))
            self.cache_data.pop(srt)
        self.history.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None
        if self.cache_data.get(key):
            self.history.remove(key)
            self.history.append(key)
            return self.cache_data.get(key)

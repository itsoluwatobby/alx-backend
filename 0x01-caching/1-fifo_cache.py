#!/usr/bin/python3
"""
FIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    An instance of FIFOCache class that inherits from the
    BaseCaching class
    """
    def __init__(self):
        """Instantiates an instance of the FIFOCache class"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data.keys()) > self.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            print('DISCARD {}'.format(keys[0]))
            del self.cache_data[keys[0]]

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None
        try:
            return self.cache_data[key]
        except Exception as e:
            return None

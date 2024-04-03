#!/usr/bin/python3
"""
FIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    An instance of LIFOCache class that inherits from the
    BaseCaching class
    """
    def __init__(self):
        """Instantiates an instance of the LIFOCache class"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.cache_data.keys()) >= self.MAX_ITEMS:
                set_key = self.stack.pop()
                print('DISCARD {}'.format(set_key))
                self.cache_data.pop(set_key)
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None
        try:
            return self.cache_data[key]
        except Exception as e:
            return None

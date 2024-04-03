#!/usr/bin/python3
"""
LFUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    An instance of LFUCache class that inherits from the
    BaseCaching class
    """
    def __init__(self):
        """Instantiates an instance of the LFUCache class"""
        super().__init__()
        self.history = []
        self.least = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if (len(self.history) >= self.MAX_ITEMS and
                not self.cache_data.get(key)):
            deleted = self.history.pop(0)
            self.least.pop(deleted)
            self.cache_data.pop(deleted)
            print('DISCARD: {}'.format(deleted))

        if self.cache_data.get(key):
            self.history.remove(key)
            self.least[key] += 1
        else:
            self.least[key] = 0

        in_index = 0
        while (in_index < len(self.history) and
                not self.least[self.history[in_index]]):
            in_index += 1
            self.history.insert(in_index, key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if self.cache_data.get(key):
            self.least[key] += 1
            if self.history.index(key) + 1 != len(self.history):
                while (self.history.index(key) + 1 < len(self.history) and
                        self.least[key] >=
                        self.least[self.history[self.history.index(key) + 1]]):
                    self.history.insert(self.history.index(key) + 1,
                                      self.history.pop(self.history.index(key)))
        return self.cache_data.get(key)

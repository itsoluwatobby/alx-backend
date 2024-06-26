#!/usr/bin/python3
"""
BaseCache module inherits from the basicCaching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    An instance of basicCache class that inherits from the
    BaseCaching class
    """
    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None

        try:
            return self.cache_data[key]
        except Exception as e:
            return None

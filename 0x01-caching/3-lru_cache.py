#!/usr/bin/python3
"""Cache replacement policies"""
from collections import deque
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """Basic cache with Limit.
    Use Least Recently Used eviction policy
    to free cache when size exceeds capacity

    Args:
        BaseCaching (class): Base Class
    """

    def __init__(self):
        """init method for the class
        """
        super().__init__()
        self.access = deque()

    def get(self, key):
        """Get item by key
        Args:
            key (Any): Index position
        """
        if key and key in self.cache_data:
            self.access.remove(key)
            self.access.append(key)
            return self.cache_data[key]
        return None

    def put(self, key, value):
        """Put value by key into cache and frequency dictionary.
        Check the capacity of the cache and delete the key-value if
        necessary
        """
        if key and value:
            if key in self.cache_data:
                self.access.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                oldest = self.access.popleft()
                print("DISCARD: {}".format(oldest))
                del self.cache_data[oldest]
            self.cache_data[key] = value
            self.access.append(key)


if __name__ == "__main__":
    my_cache = LRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()

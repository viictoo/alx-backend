#!/usr/bin/python3
"""Cache replacement policies FIFO"""
from collections import defaultdict, deque
from typing import Any, Deque
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """Basic cache with Limit.
    Use first in first out eviction policy
    to free cache when size exceeds capacity

    Args:
        BaseCaching (class): Base Class
    """

    def __init__(self):
        super().__init__()
        self.que: Deque[Any] = deque([])

    def get(self, key: Any) -> Any:
        """Get item by key
        Args:
            key (Any): Index position
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None

    def put(self, key: Any, value: Any) -> None:
        """Put value by key into cache and frequency dictionary.
        Check the capacity of the cache and delete the key-value if
        necessary
        """
        if key and value:
            if key in self.cache_data:
                self.que.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first = self.que.popleft()
                del self.cache_data[first]
                print("DISCARD: {}".format(first))
            self.que.append(key)
            self.cache_data[key] = value


if __name__ == "__main__":
    my_cache = FIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()

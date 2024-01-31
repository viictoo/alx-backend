#!/usr/bin/python3
"""Cache replacement policies"""
from collections import defaultdict, deque
from typing import Any, Tuple, Dict, Deque
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """Basic cache with no Limit

    Args:
        BaseCaching (class): Base Class
    """

    def __init__(self):
        """ init method for the class"""
        super().__init__()
        self.que: Deque[Any] = deque([])

    def get(self, key: Any) -> Any:
        """Get value by key. Updates the hits and misses statistics.

        Args:
            key (Any): Argument to function

        Returns:
            (Any)
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None

    def put(self, key: Any, value: Any) -> None:
        """Put value by key into cache and frequency dictionary.
        Check the capacity of the cache and delete the key-value if necessary.

        Args:
            key (Any): Argument to function
            value (Any): Result of function
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

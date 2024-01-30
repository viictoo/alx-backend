#!/usr/bin/python3
"""Cache replacement policies"""
BaseCaching = __import__("base_caching").BaseCaching
from typing import Any


class BasicCache(BaseCaching):
    """Basic cache with no Limit

    Args:
        BaseCaching (class): Base Class
    """

    def __init__(self):
        super().__init__()

    def get(self, key: Any) -> Any:
        """Get item by key. Updates the hits and misses statistics.

        Args:
            key (Any): Argument to function

        Returns:
            (Any)
        """
        if key in self.cache_data:
            item = self.cache_data[key]
            return item


    def put(self, key: Any, item: Any) -> None:
        """Put item by key into cache and frequency dictionary.
        Check the capacity of the cache and delete the key-item if necessary.

        Args:
            key (Any): Argument to function
            item (Any): Result of function
        """
        if key and item:
            self.cache_data[key] = item


if __name__ == "__main__":

    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))

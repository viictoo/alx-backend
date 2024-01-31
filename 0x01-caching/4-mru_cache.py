#!/usr/bin/python3
"""Cache replacement policies"""
from collections import OrderedDict, deque
from typing import Any
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    ORDERED DICT = more memory: doubly linked list
    DEQUE = LIST LIKE CONTAINER
    Args:
        BaseCaching (BASE CLASS): parent class
    """

    def __init__(self):
        super().__init__()
        self.capacity = self.MAX_ITEMS
        self.access = deque()

    def get(self, key):
        """retrieve item from cache

        Args:
            key (int): item position

        Returns:
            any: item cached at that key in the dict
        """
        if key and key in self.cache_data:
            self.access.remove(key)
            self.access.append(key)
            return self.cache_data[key]
        return None

    def put(self, key, value):
        """insert into cache

        Args:
            key (int): index
            value (any): cache item
        """
        if key in self.cache_data:
            self.access.remove(key)
        elif len(self.cache_data) >= self.capacity:
            recent = self.access.pop()
            print("DISCARD: ", recent)
            del self.cache_data[recent]
        self.cache_data[key] = value
        self.access.append(key)


if __name__ == "__main__":
    my_cache = MRUCache()
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
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()

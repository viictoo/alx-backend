#!/usr/bin/python3
"""Cache replacement policies"""
from typing import Any
from collections import deque
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    ORDERED DICT = more memory: doubly linked list
    DEQUE = LIST LIKE CONTAINER


    Args:
        BaseCaching (_type_): _description_
    """

    def __init__(self):
        """init method for the class
        """
        super().__init__()
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
        if value and  key and key in self.cache_data:
            self.access.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            oldest = self.access.popleft()
            print("DISCARD: {}".format(oldest))
            self.cache_data[oldest]
        self.cache_data[key] = value
        self.access.append(key)
    # def __init__(self):
    #     self.cache_data = OrderedDict()
    #     self.capacity = self.MAX_ITEMS

    # def get(self, key: Any) -> Any:
    #     if key not in self.cache_data:
    #         return None
    #     value = self.cache_data.pop(key)
    #     self.cache_data[key] = value
    #     return value

    # def put(self, key: Any, value: Any) -> None:
    #     if key in self.cache_data:
    #         self.cache_data.pop(key)
    #         # least = self.cache_data.pop(key)
    #         # print("DISCARD: ", least)
    #     elif len(self.cache_data) >= self.capacity:
    #         least = self.cache_data.popitem(last=False)
    #         print("DISCARD: ", least[0])
    #     self.cache_data[key] = value


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

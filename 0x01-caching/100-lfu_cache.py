#!/usr/bin/python3
""" Cache replacement policies """
from typing import Any, Dict
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Basic cache with Limit.
    Use Least Frequently Used eviction policy
    to free cache when size exceeds capacity

    Args:
        BaseCaching (class): Base Class
    """

    def __init__(self):
        """init method for the class
        """
        super().__init__()
        self.freq_dict: Dict = {}

    def get(self, key: Any) -> Any:
        """Get item by key
        Args:
            key (Any): Index position
        """
        if key and key in self.cache_data:
            self.freq_dict[key] += 1
            value = self.cache_data[key]
            return value
        return None

    def put(self, key: Any, value: Any) -> None:
        """ Put value by key into cache and frequency dictionary.
            Check the cache size and delete the key-value if necessary.
            -   discard the least frequency used item (LFU algorithm)
            -   if you there is more than 1 item to discard,
                use the LRU algorithm to discard only the least recently used
        Args:
            key (Any): cache index
            value (Any): cache data
        """
        if key and value:
            if len(self.cache_data) >= self.MAX_ITEMS:
                LFU = min(self.freq_dict, key=self.freq_dict.get)
                self.cache_data.pop(LFU)
                print("DISCARD: {}".format(LFU))
                self.freq_dict.pop(LFU)
            if key not in self.freq_dict:
                self.freq_dict[key] = 0
            self.cache_data[key] = value


if __name__ == "__main__":
    my_cache = LFUCache()
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
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()

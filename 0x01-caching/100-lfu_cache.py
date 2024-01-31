#!/usr/bin/python3
""" Cache replacement policies """
from collections import defaultdict, deque
from typing import Any, Dict, Deque
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Least Frequently Used

    Args:
        BaseCaching (class): Base Class
    """

    def __init__(self):
        """init method for the class
        """
        super().__init__()
        self.freq_dict: Dict[int, Deque[Any]] = defaultdict(lambda: deque([]))
        self.hits, self.misses, self.curr_size = 0, 0, 0

    def print_cache(self):
        """ Print the cache items from the custom dict
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)[0]))

    def update(self, key: Any, value: Any) -> None:
        """Update frequency of key in cache and frequency dictionary.
        Removes key in frequency dictionary if necessary.

        Args:
            key (Any): Argument to function
            value (Any): Result of function
        """
        _, freq = self.cache_data[key]
        self.cache_data[key] = (value, freq + 1)
        self.freq_dict[freq].remove(key)
        self.freq_dict[freq + 1].append(key)
        if not len(self.freq_dict[freq]):
            del self.freq_dict[freq]

    def get(self, key: Any) -> Any:
        """Get value by key. Updates the hits and misses statistics.

        Args:
            key (Any): Argument to function

        Returns:
            (Any)
        """
        if key and key in self.cache_data:
            self.hits += 1
            value = self.cache_data[key][0]
            self.update(key, value)
            return value
        self.misses += 1
        return None

    def put(self, key: Any, value: Any) -> None:
        """Put value by key into cache and frequency dictionary.
        Check the capacity of the cache and delete the key-value if necessary.

        Args:
            key (Any): Argument to function
            value (Any): Result of function
        """
        if key in self.cache_data:
            self.update(key, value)
        else:
            self.cache_data[key] = (value, 1)
            self.freq_dict[1].append(key)
            self.curr_size += 1
            if self.MAX_ITEMS is not None and self.curr_size > self.MAX_ITEMS:
                remove_key = self.freq_dict[min(self.freq_dict)].popleft()
                print("DISCARD: ", remove_key)
                del self.cache_data[remove_key]
                self.curr_size -= 1


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

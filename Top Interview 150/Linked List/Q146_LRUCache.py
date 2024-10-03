from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        # self.order = []  # O(n)

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # last

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # FIFO

# Testcase
obj = LRUCache(2)
print(obj.put(1, 1))
print(obj.put(2, 2))
print(obj.get(1))
print(obj.put(3, 3))
print(obj.get(2))
print(obj.put(4, 4))
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
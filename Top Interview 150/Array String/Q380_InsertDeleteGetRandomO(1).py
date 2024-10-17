from typing import List
import random

class RandomizedSet:

    def __init__(self):
        self.obj = {}
        return

    def insert(self, val: int) -> bool:
        if val not in self.obj:
            self.obj[val] = val
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.obj:
            return False
        else:
            del self.obj[val]
            return True

    def getRandom(self) -> int:
        return random.choice(list(self.obj.keys()))

# Testcase
task = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
vals = [[], [1], [2], [2], [], [1], [2], []]

for i in range(len(task)):
    if task[i] == "RandomizedSet":
        obj = RandomizedSet()
    elif task[i] == "insert":
        print(obj.insert(vals[i][0]))
    elif task[i] == "remove":
        print(obj.remove(vals[i][0]))
    elif task[i] == "getRandom":
        print(obj.getRandom())
    else:
        print("Invalid task")
from collections import deque
from random import randint


class RandomizedSet:

    def __init__(self):
        self.ans = set()
        self.nums = deque()

    def insert(self, val: int) -> bool:
        if val not in self.ans:
            self.ans.add(val)
            self.nums.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.ans:
            self.ans.remove(val)
            self.nums.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        n = len(self.ans)
        random = randint(0, n - 1)
        return self.nums[random]

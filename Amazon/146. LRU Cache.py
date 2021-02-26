from collections import OrderedDict
from random import choice

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.ans = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.ans:
            self.ans.move_to_end(key)
            return self.ans[key]
        else:
            return -1

    def put(self, key: int, val: int) -> None:
        if key in self.ans:
            del self.ans[key]
        elif len(self.ans) >= self.size:
            self.ans.popitem(last=False)

        self.ans[key] = val

from random import randint


class RandomizedSet:

    def __init__(self):
        self.ans = set()
        self.nums = []

    def insert(self, val: int) -> bool:
        flag = False

        if val not in self.ans:
            flag = True
            self.nums.append(val)
            self.ans.add(val)

        return flag

    def remove(self, val: int) -> bool:
        flag = False
        if val in self.ans:
            flag = True
            self.nums.remove(val)
            self.ans.remove(val)

        return flag

    def getRandom(self) -> int:
        return self.nums[randint(0, len(self.nums) - 1)]

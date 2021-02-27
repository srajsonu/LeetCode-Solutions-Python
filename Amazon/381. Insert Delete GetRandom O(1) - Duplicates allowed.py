from random import randint


class RandomizedCollection:

    def __init__(self):
        self.freq = {}
        self.ans = []

    def insert(self, val: int) -> bool:
        if val not in self.freq:
            self.freq[val] = 1
            self.ans.append(val)
            return True
        else:
            self.freq[val] += 1
            self.ans.append(val)
            return False

    def remove(self, val: int) -> bool:
        if val in self.freq:
            if self.freq[val] > 1:
                self.freq[val] -= 1
                self.ans.remove(val)
            else:
                self.freq.pop(val)
                self.ans.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        n = len(self.ans)
        rand = randint(0, n - 1)
        return self.ans[rand]

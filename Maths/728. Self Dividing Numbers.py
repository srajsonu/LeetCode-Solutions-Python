from typing import List
from binarytree import build


class Solution:
    def check(self, num):
        for i in str(num):
            if i == '0' or num % int(i) > 0:
                return False
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            if self.check(i):
                ans.append(i)

        return ans

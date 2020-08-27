from collections import deque
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = deque()
        ans = []
        e = target[-1]

        for i in range(1, e + 1):
            if i in target:
                ans.append('Push')
            else:
                ans.append('Push')
                ans.append('Pop')

        return ans

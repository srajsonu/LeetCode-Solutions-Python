from typing import List


class Solution:
    def numIdenticalPairs(self, A: List[int]) -> int:
        n = len(A)
        count = {}
        ans = 0
        for i in A:
            if i not in count:
                count[i] = 1
            else:
                ans += count[i]
                count[i] += 1

        return ans

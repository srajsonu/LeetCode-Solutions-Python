from typing import List


class Solution:
    def distributeCandies(self, candies: int, n: int) -> List[int]:
        ans = [0 for _ in range(n)]
        i = 0
        while candies > 0:
            ans[i % n] += min(candies, i + 1)
            candies -= i + 1
            i += 1

        return ans

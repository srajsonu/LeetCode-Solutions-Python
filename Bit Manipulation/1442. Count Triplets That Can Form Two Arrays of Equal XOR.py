from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count, n = 0, len(arr)
        for i in range(n - 1):
            accu = arr[i]
            for k in range(i + 1, n):
                if not accu ^ arr[k]:
                    count += k - i
        return count

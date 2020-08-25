from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        ans = []
        xor = [0 for _ in range(n)]
        xor[0] = arr[0]
        for i in range(1, n):
            xor[i] = arr[i] ^ xor[i - 1]

        for i, j in queries:
            if i == 0:
                xor_query = xor[j]
            else:
                xor_query = xor[j] ^ xor[i - 1]
            ans.append(xor_query)
        return ans

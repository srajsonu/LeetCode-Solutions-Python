from heapq import *


class Solution:
    def kClosest(self, A, B):
        if not A or not B:
            return []
        pq = []

        for i, j in A:
            heappush(pq, (i ** 2 + j ** 2, i, j))

        ans = []
        while B:
            i, j, k = heappop(pq)
            ans.append([j, k])
            B -= 1

        return ans

if __name__ == '__main__':
    A = [[1, 3], [-2, 2]]
    B = 1
    C = Solution()
    print(C.kClosest(A, B))

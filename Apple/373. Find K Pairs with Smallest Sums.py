from heapq import *
class Solution:
    def kSmallestPairs(self, A, B, k):
        if not A or not B: return []
        m = len(A)
        n = len(B)
        heap = []
        for i in range(m):
            for j in range(n):
                heappush(heap, (A[i]+B[j], [A[i], B[j]]))

        ans = []
        for i in range(len(heap)):
            if k <= 0: break
            sm, val = heappop(heap)
            ans.append(val)
            k -= 1

        return ans


if __name__ == '__main__':
    A = [1, 7, 11]
    B = [2, 4, 6]
    C = 3
    D = Solution()
    print(D.kSmallestPairs(A, B, C))

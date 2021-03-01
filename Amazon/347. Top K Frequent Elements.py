from heapq import *


class Solution:
    def topKFrequent(self, A, B):
        freq = {}
        for i in A:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        pq = []
        for i in freq:
            heappush(pq, (-freq[i], i))

        ans = []
        while B:
            i, j = heappop(pq)
            ans.append(j)
            B -= 1

        return ans


if __name__ == '__main__':
    A = [1, 1, 1, 2, 2, 3]
    B = 2
    C = Solution()
    print(C.topKFrequent(A, B))

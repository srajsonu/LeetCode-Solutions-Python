from collections import defaultdict
from heapq import *


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = defaultdict(list)
        dis = [float('inf') for _ in range(n)]
        for i, j, k in flights:
            graph[i].append((j, k))

        pq = []
        heappush(pq, (0, src, K))
        while pq:
            dist, node, K = heappop(pq)
            if node == dst:
                return dist
            if K >= 0:
                for v, w in graph[node]:
                    new_dis = dist + w
                    heappush(pq, (new_dis, v, K - 1))

        return dis[dst] if dis[dst] != float('inf') else -1

if __name__ == '__main__':
    n = 3
    edges = [[0, 1, 100],
             [1, 2, 100],
             [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    A = Solution()
    print(A.findCheapestPrice(n,edges,src,dst,k))

from heapq import *
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times, N, K):
        graph = defaultdict(list)
        dis = [float('inf') for _ in range(N)]
        vis = [False for _ in range(N)]

        for i, j, k in times:
            graph[i - 1].append((j - 1, k))

        pq = []
        heappush(pq, (0, K - 1))
        dis[K - 1] = 0

        while pq:
            dist, node = heappop(pq)
            vis[node] = True

            for v, w in graph[node]:
                new_dis = dist + w
                if new_dis < dis[v]:
                    dis[v] = new_dis
                    heappush(pq, (new_dis, v))

        ans = max(dis)
        return ans if ans != float('inf') else -1

if __name__ == '__main__':
    times = [[2, 1, 1],
             [2, 3, 1],
             [3, 4, 1]]
    N = 4
    K = 2
    C = Solution()
    print(C.networkDelayTime(times,N,K))

from collections import defaultdict, deque
from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]: #Brute force O(N^2)
        graph = defaultdict(list)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        ans = []
        for i in range(N):
            q = deque()
            q.append((i, 0))
            level = 0
            vis = [False for _ in range(N)]
            tmp = 0
            while q:
                size = len(q)
                for _ in range(size):
                    node, pos = q.popleft()
                    vis[node] = True
                    tmp += level
                    for elem in graph[node]:
                        if not vis[elem]:
                            vis[elem] = True
                            q.append((elem, pos + 1))
                level += 1
            ans.append(tmp)
        return ans

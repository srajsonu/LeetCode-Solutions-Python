from collections import defaultdict, deque


class Solution:
    def canFinish(self, A, B):
        graph = defaultdict(list)

        for i, j in B:
            graph[i].append(j)

        inDegree = [0 for _ in range(A)]

        for i in graph:
            for j in graph[i]:
                inDegree[j] += 1

        q = deque()
        for i in range(A):
            if inDegree[i] == 0:
                q.append(i)

        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for nxt in graph[curr]:
                inDegree[nxt] -= 1
                if inDegree[nxt] == 0:
                    q.append(nxt)

        return True if len(ans) == A else False

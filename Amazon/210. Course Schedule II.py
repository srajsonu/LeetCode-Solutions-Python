from collections import defaultdict, deque


class Solution:
    def findOrder(self, A, B):
        graph = defaultdict(list)
        inDegree = {}
        q = deque()

        for i in range(A):
            inDegree[i] = 0

        for i, j in B:
            graph[j].append(i)
            inDegree[i] += 1

        for i in inDegree:
            if inDegree[i] == 0:
                q.append(i)

        ans = []
        while q:
            i = q.popleft()
            ans.append(i)

            for j in graph[i]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    q.append(j)

        return ans if len(ans) == A else []

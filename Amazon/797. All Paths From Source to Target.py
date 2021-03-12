from collections import defaultdict


class Solution:
    def dfs(self, s, d, path):
        path.append(s)
        if s == d:
            self.ans.append(path[:])
            path.pop()
            return

        for nxt_node in self.graph[s]:
            self.dfs(nxt_node, d, path)

        path.pop()
        return path

    def allPathsSourceTarget(self, A):
        n = len(A)
        s = 0
        d = n - 1

        self.graph = defaultdict(list)

        for i in range(n):
            for j in range(len(A[i])):
                self.graph[i].append(A[i][j])

        self.ans = []
        self.dfs(s, d, [])
        return self.ans


if __name__ == '__main__':
    A = [[1, 2], [3], [3], []]
    B = Solution()
    print(B.allPathsSourceTarget(A))

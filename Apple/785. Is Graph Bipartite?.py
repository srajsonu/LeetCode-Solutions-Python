from collections import deque
class Solution:
    def isValid(self, graph, v, color, colors):
        if colors[v] != 0:
            return colors[v] == color

        colors[v] = color
        for node in graph[v]:
            if not self.isValid(graph, node, -color, colors):
                return False

        return True
    
    def solve(self, A):
        n = len(A)
        colors = [0 for _ in range(n)]
        q = deque()

        for i in range(n):
            if colors[i] != 0:
                continue

            q.append((i, 1))
            while q:
                curr, color = q.popleft()
                colors[curr] = color

                for node in A[curr]:
                    if colors[node] == 0:
                        colors[node] = -color
                        q.append((node, -color))

                    elif colors[node] == colors[curr]:
                        return False

        return True

if __name__ == '__main__':
    A = [[1,3],
         [0,2],
         [1,3],
         [0,2]]

    B = Solution()
    print(B.solve(A))

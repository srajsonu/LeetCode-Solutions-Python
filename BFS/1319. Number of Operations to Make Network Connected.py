from collections import defaultdict, deque


class Solution:
    def find_root(self, A, parent):
        if parent[A] == A:
            return A
        return self.find_root(parent[A], parent)

    def union(self, A, B, parent, height):
        C = self.find_root(A, parent)
        D = self.find_root(B, parent)

        if C == D:
            return

        if height[C] < height[D]:
            parent[C] = D
        elif height[C] > height[D]:
            parent[D] = C
        else:
            parent[D] = C
            height[C] += 1

    def makeConnected(self, A, B):
        if len(B) < A - 1: return -1
        parent = [i for i in range(A)]
        height = [0 for _ in range(A)]

        for i, j in B:
            C = self.find_root(i, parent)
            D = self.find_root(j, parent)

            if C == D:
                continue

            self.union(C, D, parent, height)

        count = 0
        for i in range(A):
            if parent[i] == i:
                count += 1

        return count - 1

    def Solve(self, A, B):
        graph = defaultdict(list)

        for i,j in B:
            graph[i].append(j)
            graph[j].append(i)

        q = deque()
        vis = [False for _ in range(A)]
        count = 0
        for i in range(A):
            if not vis[i]:
                q.append(i)

                while q:
                    j, t = q.popleft()
                    vis[j] = True
                    for node in graph[j]:
                        if not vis[node]:
                            vis[node] = True
                            q.append(node)
                count += 1

        return count-1

if __name__ == '__main__':
    A = 4
    B = [[0, 1], [0, 2], [1, 2]]
    C = Solution()
    print(C.Solve(A,B))
    print(C.makeConnected(A, B))

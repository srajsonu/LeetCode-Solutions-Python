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

        self.count -= 1

    def Solve(self, A):
        m = len(A)
        n = len(A[0])

        parent = [i for i in range(4 * m * n)]
        height = [0 for _ in range(4 * m * n)]
        self.count = 4 * m * n

        def g(i, j, k):
            return (i * n + j) * 4 + k

        for i in range(m):
            for j in range(n):
                if A[i][j] != '/':
                    self.union(g(i, j, 0), g(i, j, 1), parent, height)
                    self.union(g(i, j, 2), g(i, j, 3), parent, height)

                if A[i][j] != '\ ':
                    self.union(g(i, j, 0), g(i, j, 3), parent, height)
                    self.union(g(i, j, 2), g(i, j, 1), parent, height)

                if i > 0:
                    self.union(g(i - 1, j, 2), g(i, j, 0), parent, height)

                if j > 0:
                    self.union(g(i, j - 1, 1), g(i, j, 3), parent, height)

        return self.count


if __name__ == '__main__':
    A = [['/'], ['/']]
    B = Solution()
    print(B.Solve(A))

class Solution:
    def dfs(self, A, B, i, j, count):
        if count == len(B):
            return True

        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] != B[count]:
            return False

        tmp = A[i][j]
        A[i][j] = ''

        ans = self.dfs(A, B, i + 1, j, count + 1) \
              or self.dfs(A, B, i, j + 1, count + 1) \
              or self.dfs(A, B, i - 1, j, count + 1) \
              or self.dfs(A, B, i, j - 1, count + 1)

        A[i][j] = tmp
        return ans

    def exist(self, A, B):
        m = len(A)
        n = len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j] == B[0] and self.dfs(A, B, i, j, 0):
                    return True

        return False


if __name__ == '__main__':
    A = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    B = "ABCB"
    C = Solution()
    print(C.exist(A, B))

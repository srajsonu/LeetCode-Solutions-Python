class Solution:
    def numSubmat(self, A):
        m = len(A)
        n = len(A[0])

        for i in range(1, m):
            for j in range(n):
                if A[i][j] == 0:
                    continue
                A[i][j] += A[i - 1][j]

        ans = 0
        for i in range(m):
            stack = []
            cnt = 0
            for j in range(n):
                while stack and A[i][stack[-1]] > A[i][j]:
                    jj = stack.pop()
                    kk = stack[-1] if stack else -1
                    cnt -= (A[i][jj] - A[i][j]) * (jj - kk)

                cnt += A[i][j]
                ans += cnt
                stack.append(j)

        return ans

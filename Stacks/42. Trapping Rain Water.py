class Solution:
    def trap(self, A):
        n = len(A)
        l = [0 for _ in range(n)]
        r = [0 for _ in range(n)]

        for i in range(1, n):
            l[i] = max(A[i - 1], l[i - 1])

        for i in reversed(range(n - 1)):
            r[i] = max(A[i + 1], r[i + 1])

        ans = 0
        for i in range(n):
            tmp = min(l[i], r[i]) - A[i]
            if tmp < 0:
                continue
            ans += tmp

        return ans

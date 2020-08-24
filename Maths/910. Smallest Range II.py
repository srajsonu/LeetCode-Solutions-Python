class Solution:
    def smallestRangeII(self, A, K):
        n = len(A)
        A.sort()
        mn, mx = A[0], A[-1]
        ans = mx - mn
        for i in range(n - 1):
            a, b = A[i], A[i + 1]
            ans = min(ans, max(mx - K, a + K) - min(mn + K, b - K))

        return ans

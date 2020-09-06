class Solution:
    def findLengthOfShortestSubarray(self, A):
        if not A: return 0
        n = len(A)
        l = 0
        while l + 1 < n and A[l] <= A[l + 1]:
            l += 1

        if l == n - 1: return 0

        r = n - 1

        while r > l and A[r - 1] <= A[r]:
            r -= 1

        ans = min(n - l - 1, r)

        i = 0
        j = r

        while i <= l and j < n:
            if A[j] >= A[i]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1

        return ans

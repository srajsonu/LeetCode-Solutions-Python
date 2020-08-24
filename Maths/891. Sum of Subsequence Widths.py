class Solution:
    def sumSubseqWidths(self, A):
        mod = 10 ** 9 + 7
        n = len(A)
        A.sort()

        pow2 = [1]
        for i in range(1, n):
            pow2.append(pow2[-1] * 2 % mod)

        ans = 0
        for i, j in enumerate(A):
            ans += (pow2[i] - pow2[n - 1 - i]) * j
            ans %= mod

        return ans

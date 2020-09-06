class Solution:
    def kadane(self, A):
        curr = 0
        mx = 0
        for i in A:
            curr = max(i, curr + i)
            mx = max(mx, curr)

        return mx

    def kConcatenationMaxSum(self, arr, k):
        mod = 10 ** 9 + 7
        if k == 1:
            return self.kadane(arr) % mod
        else:
            if sum(arr) <= 0:
                return self.kadane(arr * 2) % mod
            else:
                return ((k - 1) * sum(arr) + self.kadane(arr)) % mod

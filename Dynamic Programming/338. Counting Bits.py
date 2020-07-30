class Solution:
    def countBits(self, A):
        dp = [0 for _ in range(A + 1)]
        offset = 1
        for i in range(1, A + 1):
            if offset * 2 == i:
                offset *= 2
            dp[i] = dp[i - offset] + 1
        return dp


if __name__ == '__main__':
    A = 5
    B = Solution()
    print(B.countBits(A))

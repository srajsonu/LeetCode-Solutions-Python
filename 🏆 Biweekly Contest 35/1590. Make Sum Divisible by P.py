class Solution:
    def solve(self, A, p):
        n = len(A)
        sm = sum(A)
        r = sm % p

        dp = {}
        curr = 0
        ans = len(A)

        for i,j in enumerate(A):
            curr = (curr + j) % p
            dp[curr] = i
            if (curr - r) % p in dp:
                ans = min(ans, i - dp[(curr - r) % p])

        return ans if ans < n else -1

if __name__ == '__main__':
    A = [3,1,4,2]
    p = 6
    B = Solution()
    print(B.solve(A, p))

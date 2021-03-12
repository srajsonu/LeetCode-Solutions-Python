class Solution:
    def dp(self, A, i, dp):
        if dp[i]:
            return dp[i]

        if i >= len(A)-1:
            return 0

        ans = float('inf')
        max_jump = A[i]
        while max_jump:
            ans = min(ans, 1 + self.dp(A, i + max_jump, dp))
            max_jump -= 1

        dp[i] = ans
        return ans

    def jump(self, A):
        n = len(A)
        m = max(A)
        dp = [0 for _ in range(n+m)]
        return self.dp(A, 0, dp)

    def solve(self, A): #greedy Algorithm
        n = len(A)
        ladder = A[0]
        stairs = A[0]

        jump = 1
        for i in range(1, n-1):
            if i + A[i] > ladder:
                ladder = i + A[i]

            stairs -= 1
            if stairs == 0:
                jump += 1
                stairs = ladder - i

        return jump

if __name__ == '__main__':
    A = [2, 3, 1, 1, 4]
    B = Solution()
    print(B.jump(A))
    print(B.solve(A))

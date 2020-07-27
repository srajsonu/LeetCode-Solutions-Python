class Solution:
    def isPalindrome(self, A, i, j, dp):
        if i > j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if i == j:
            dp[i][j] = 1

        elif A[i] == A[j] and self.isPalindrome(A,i+1,j-1,dp) and j - i > 1:
            if self.max < j-i+1:
                self.max = j-i+1
                self.start = i

            dp[i][j] = 2 + self.isPalindrome(A,i+1,j-1,dp)

        elif A[i] == A[j] and j - i <= 1:
            if self.max < j - i + 1:
                self.max = j - i
                self.start = i
            dp[i][j] = 2

        elif A[i] != A[j]:
            dp[i][j] = max(self.isPalindrome(A,i+1,j,dp), self.isPalindrome(A,i,j-1,dp))

        return dp[i][j]

    def Solve(self, A):
        self.max = 0
        self.start = 0
        n = len(A)
        dp = [[-1] * n for _ in range(n)]
        self.isPalindrome(A,0,n-1,dp)
        return  self.start, self.max, A[self.start:self.max+1],dp

    def lps(self,A):
        n = len(A)
        dp = [[False]*n for _ in range(n)]
        ans = ""
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if A[i] == A[j] and j-i <= 2 or dp[i+1][j-1]:
                    dp[i][j] = True

                if dp[i][j] and (not ans or j-i+1 > len(ans)):
                    ans = A[i:j+1]
        return ans


if __name__ == '__main__':
    A = "cbbd"
    B = Solution()
    print(B.Solve(A))
    print(B.lps(A))

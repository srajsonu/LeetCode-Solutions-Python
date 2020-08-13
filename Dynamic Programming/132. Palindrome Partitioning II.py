class Solution:
    def isPalindrome(self,s,i,j):
        return s[i:j+1] == s[i:j+1][::-1]

    def dp(self,s,index,dp):
        if index >= len(s) or self.isPalindrome(s,index, len(s)-1):
            return 0

        if index in dp:
            return dp[index]

        ans = float('inf')
        for i in range(index, len(s)+1):
            if i != len(s) and self.isPalindrome(s,index,i):
                ans = min(ans, 1 + self.dp(s,i+1,dp))

        dp[index] = ans
        return ans

    def Solve(self,A):
        n = len(A)
        dp = {}
        if self.isPalindrome(A,0,n-1):
            return 0
        return self.dp(A,0,dp), dp

    def minCut(self, s):
        n = len(s)
        dp = [i-1 for i in range(n+1)]
        return dp

if __name__ == '__main__':
    A = 'abaa'
    B = Solution()
    print(B.Solve(A))
    print(B.minCut(A))

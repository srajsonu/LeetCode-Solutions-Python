from math import ceil
class Solution:
    def dp(self,n,index,pdt,dp):
        if index == n:
            return pdt

        if index > n: return 0

        key = str(index)+" -> "+str(pdt)

        if key in dp:
            return dp.get(key)

        tmp = float('-inf')
        for i in range(1,ceil(n/2)+1):
            tmp = max(tmp, self.dp(n,index+i,pdt*i,dp))

        dp[key] = tmp
        return tmp

    def Solve(self,A):
        dp = {}
        return self.dp(A,0,1,dp),dp

    def integerBreak(self,n):
        if n <= 2: return 1
        dp = [0 for _ in range(n+1)]
        dp[1] = 0
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(1,i//2+1):
                dp[i] = max(dp[i], max(j*(i-j), j*dp[i-j]))

        return dp[-1]


if __name__ == '__main__':
    A = 10
    B = Solution()
    print(B.Solve(A))
    print(B.integerBreak(A))

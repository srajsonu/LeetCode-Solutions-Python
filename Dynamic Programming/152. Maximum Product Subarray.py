class Solution:
    def product(self,A):     #Brute-Force
        ans = 1
        for i in A:
            ans *= i
        return ans

    def dp(self,A, dp):
        if len(A) == 0:
            return True

        for i in range(1,len(A)+1):
            print(A[:i])
            pdt = self.product(A[:i])
            self.ans = max(self.ans,pdt)
            self.dp(A[i:],dp)

        return False

    def Solve(self,A):
        self.ans = float('-inf')
        dp = []
        self.dp(A,dp)
        return self.ans

    def maxProduct(self,A):    #Optimized
        n = len(A)
        maxDP = A[0]
        minDP = A[0]
        ans = A[0]
        for i in range(1,n):
            if A[i] >= 0:
                maxDP = max(maxDP*A[i],A[i])
                minDP = min(minDP*A[i],A[i])
            else:
                maxDP_old = maxDP
                maxDP = max(A[i], minDP*A[i])
                minDP = min(maxDP_old*A[i],A[i])

            ans = max(maxDP,ans)

        return ans

if __name__ == '__main__':
    A = [2,3,-2,4]
    B = Solution()
    print(B.Solve(A))
    print(B.maxProduct(A))

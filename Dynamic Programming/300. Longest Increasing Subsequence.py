class Solution:
    def recursive(self,A,index,prev):  #Brute-Force
        if index == len(A):
            return 0

        pick = 0
        if A[index] > prev:
            pick = 1 + self.recursive(A,index+1,A[index])

        dont = self.recursive(A,index+1,prev)
        return max(pick,dont)

    def dp(self,A,index,prev_index,dp):  #Top-Down DP
        if index == len(A):
            return 0

        if dp[prev_index][index]:
            return dp[prev_index][index]

        pick = 0
        if prev_index < 0 or A[index] > A[prev_index]:
            pick = 1 + self.dp(A,index+1,index,dp)

        dont = self.dp(A,index+1,prev_index,dp)
        dp[prev_index][index] = max(pick,dont)

        return dp[prev_index][index]


    def Solve(self,A):
        n = len(A)
        dp = [[0]*n for _ in range(n)]
        return self.dp(A,0,-1,dp)

    def lengthOfLIS(self,A): #Bottom-Up DP
        n = len(A)
        if n == 0: return 0
        dp = [1 for _ in range(n+1)]
        for i in range(1,n):
            for j in range(i):
                if A[i] > A[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

    def solve(self,A):  #Binary-Search + DP
        n = len(A)
        dp = [0 for _ in range(n)]
        ans = 0
        for x in A:
            i = 0
            j = ans
            while i != j:
                mid = (i+j)//2
                if dp[mid] < x:
                    i = mid + 1
                else:
                    j = mid
            dp[i] = x
            ans = max(ans,i+1)

        return ans

if __name__ == '__main__':
    A = [10,9,2,5,3,7,101,18]
    C = [3,5,6,2,5,4,19,5,6,7,12]
    B = Solution()
    print(B.solve(C))
    print(B.lengthOfLIS(C))

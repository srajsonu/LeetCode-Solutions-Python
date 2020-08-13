class Solution:
    def dp(self,A,index,dp):
        if index == len(A):
            if len(dp) >= 3:
                print(dp)
            return

        # for i in range(index,len(A)):
        #     self.dp(A,i+1,dp + [A[i]])

        pick = self.dp(A,index+1,dp+[A[index]])
        dont = self.dp(A,index+1,dp)
        return pick and dont

    def Solve(self,A):
        return self.dp(A,0,[])

if __name__ == '__main__':
    A = [1, 2, 3, 4]
    B = Solution()
    print(B.Solve(A))

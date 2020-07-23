class Solution:
    def Solve(self,A):
        ans = []
        for i in range(2**A):
            ans.append(i^i//2)
        return ans

if __name__ == '__main__':
    A = 3
    B = Solution()
    print(B.Solve(A))

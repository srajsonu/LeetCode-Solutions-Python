class Solution:
    def Solve(self,A):
        return A%2 == 0

if __name__ == '__main__':
    A = 3
    B = Solution()
    print(B.Solve(A))

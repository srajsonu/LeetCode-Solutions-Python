from math import factorial
class Solution:
    def Solve(self,n):
        if n == 0: return 1
        ans = 10
        for i in range(2,n+1):
            ans += 9 * factorial(9) // factorial(9-i+1)
        return ans


if __name__ == '__main__':
    A = 3
    B = Solution()
    print(B.Solve(A))

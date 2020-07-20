from math import factorial
class Solution:
    def permutations(self,digits, fact, n, k):
        if n == 1:
            self.ans += digits[-1]
            return

        f = factorial(n-1)
        index = k // f

        if k%f == 0:
            index -= 1

        self.ans += digits[index]
        digits.pop(index)
        k -= f * index
        self.permutations(digits, fact,n-1,k)

    def Solve(self,A,B):
        self.ans = ""
        digits = [str(i) for i in range(1,A+1)]
        fact = [factorial(i) for i in range(A+1)]
        self.permutations(digits, fact, A,B)
        return self.ans

if __name__ == '__main__':
    A = 4
    B = 9
    C = Solution()
    print(C.Solve(A,B))

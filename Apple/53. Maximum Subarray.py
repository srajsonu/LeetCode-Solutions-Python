class Solution:
    def solve(self, A):
        n = len(A)
        for i in range(1, n):
            if A[i-1] > 0:
                A[i] += A[i-1]

        return max(A)

if __name__ == '__main__':
    A = [-2,1,-3,4,-1,2,1,-5,4]
    B = Solution()
    print(B.solve(A))

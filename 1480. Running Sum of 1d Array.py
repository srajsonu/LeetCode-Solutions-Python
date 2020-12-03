class Solution:
    def runningSum(self, A):
        n = len(A)
        for i in range(1, n):
            A[i] += A[i-1]

        return A

if __name__ == '__main__':
    A = [1, 2, 3, 4]
    B = Solution()
    print(B.runningSum(A))

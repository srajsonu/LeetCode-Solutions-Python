class Solution:
    def productExceptSelf(self, A):
        n = len(A)
        l = [0 for _ in range(n)]
        r = [0 for _ in range(n)]

        l[0] = 1
        for i in range(1, n):
            l[i] = A[i-1] * l[i-1]

        r[n-1] = 1
        for i in reversed(range(n-1)):
            r[i] = r[i+1] * A[i+1]

        for i in range(n):
            A[i] = l[i] * r[i]

        return A


if __name__ == '__main__':
    A = [1,2,3,4]
    B = Solution()
    print(B.productExceptSelf(A))

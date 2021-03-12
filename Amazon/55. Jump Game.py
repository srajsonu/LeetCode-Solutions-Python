class Solution:
    def canJump(self, A):
        n = len(A)
        d = n - 1

        for i in range(n):
            if i + A[i] >= d:
                d = i

        return d == 0

if __name__ == '__main__':
    A = [2, 3, 1, 1, 4]
    B = Solution()
    print(B.canJump(A))

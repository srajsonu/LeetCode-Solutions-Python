class Solution:
    def dp(self, A, i, x, dir, dp):
        if i == x:
            return 0

        if i < 0:
            return float('inf')

        if i > x:
            return float('inf')

        if i in A:
            return -1

        forward = self.dp(A, i + self.a, x, dir, dp)
        backward = self.dp(A, i - self.b, x, dir, dp)
        return 1 + min(forward, backward)

    def solve(self, A, a, b, x):
        self.a = a
        self.b = b
        dp = {}
        return self.dp(A, 0, x, 0, dp)

if __name__ == '__main__':
    S = Solution()
    forbidden = [14, 4, 18, 1, 15]
    a = 3
    b = 15
    x = 9
    print(S.solve(forbidden, a, b, x))

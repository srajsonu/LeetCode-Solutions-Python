class Solution:
    def dp(self, A, pos, target, jump, dp):
        if (pos, jump) in dp:
            return False

        if jump <= 0 or pos not in A:
            return False

        if pos == target:
            return True

        row = [jump - 1, jump, jump + 1]
        for r in row:
            if self.dp(A, pos + r, target, r, dp):
                return True

        dp.add((pos, jump))
        return False

    def solve(self, A):
        target = A[-1]
        dp = set()
        return self.dp(set(A), 1, target, 1, dp)

if __name__ == '__main__':
    A = [0,1,3,5,6,8,12,17]
    B = Solution()
    print(B.solve(A))

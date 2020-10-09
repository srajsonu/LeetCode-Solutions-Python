class Solution:
    def reverse(self, A: int) -> int:
        res = 0
        if A > 0:
            while A:
                r = A % 10
                res = res * 10 + r
                A = A // 10
            if abs(res) > 2 ** 31:
                return 0
            return res
        elif A < 0:
            while A:
                r = abs(A) % 10
                res = res * 10 + r
                A = abs(A) // 10
            if abs(res) > 2 ** 31:
                return 0
            else:
                return "-" + str(res)

        elif abs(A) > 2 ** 31:
            return 0
        elif A == 0:
            return 0

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = int(num ** 0.5) + 1
        for i in range(n):
            if i * i == num:
                return True
        return False

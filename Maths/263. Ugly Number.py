class Solution:
    def divide(self, A, B):
        while A % B == 0:
            A = A / B
        return A

    def isUgly(self, num: int) -> bool:
        if num == 0: return 0
        num = self.divide(num, 2)
        num = self.divide(num, 3)
        num = self.divide(num, 5)

        return True if num == 1 else False

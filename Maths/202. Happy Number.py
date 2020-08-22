class Solution:
    def find_sum(self, A):
        total = 0
        while A > 0:
            digit = A % 10
            total += digit ** 2
            A //= 10
        return total

    def isHappy(self, n: int) -> bool:
        ans = set()
        while n and n not in ans:
            ans.add(n)
            n = self.find_sum(n)
        return n == 1

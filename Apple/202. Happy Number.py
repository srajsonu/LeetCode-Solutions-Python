class Solution:
    def find_sum(self, n):
        ans = 0
        while n:
            digit = n % 10
            ans += digit ** 2
            n //= 10
        return ans

    def isHappy(self, n: int) -> bool:
        ans = set()
        while n and n not in ans:
            ans.add(n)
            n = self.find_sum(n)
        return n == 1

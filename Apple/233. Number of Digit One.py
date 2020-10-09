class Solution:
    def countDigitOne(self, n: int) -> int:
        ones = 0
        m = r = 1
        while n > 0:
            ones += (n + 8) // 10 * m + (n % 10 == 1) * r
            r += n % 10 * m
            m *= 10
            n //= 10
        return ones


if __name__ == '__main__':
    A = 100
    B = Solution()
    print(B.countDigitOne(A))

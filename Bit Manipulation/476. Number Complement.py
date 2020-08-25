class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num).replace('0b', '')
        num = [i for i in num]
        ans = ''
        for i in num:
            if i == '1':
                ans += '0'
            else:
                ans += '1'

        return int(ans, 2)

    def solve(self, num: int) -> int:
        i = 1
        while i <= num:
            i <<= 1
        return (i - 1) ^ num

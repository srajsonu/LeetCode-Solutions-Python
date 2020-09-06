class Solution:
    def numWays(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        ones = s.count('1')

        if ones % 3 != 0: return 0
        if ones == 0: return ((n - 2) * (n - 1) // 2) % mod

        ones //= 3
        cnt, l, h = 0, 0, 0

        for c in s:
            if c == '1':
                cnt += 1
            if cnt == ones:
                l += 1

            if cnt == 2 * ones:
                h += 1

        return (l * h) % mod

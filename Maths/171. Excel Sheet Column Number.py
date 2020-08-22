class Solution:
    def titleToNumber(self, s: str) -> int:
        count = 0
        for i in s:
            count = count * 26 + (ord(i) - ord('A')) + 1
        return count

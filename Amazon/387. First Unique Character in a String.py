class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for i in range(n):
            if freq[s[i]] == 1:
                return i

        return -1

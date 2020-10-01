class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for i, j in enumerate(s):
            if freq[j] == 1:
                return i

        return -1

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        s1 = s[:n // 2]
        s2 = s[n // 2:]
        cnt1 = 0
        cnt2 = 0
        for i, j in zip(s1, s2):
            if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
                cnt1 += 1
            if j.lower() == 'a' or j.lower() == 'e' or j.lower() == 'i' or j.lower() == 'o' or j.lower() == 'u':
                cnt2 += 1

        return cnt1 == cnt2

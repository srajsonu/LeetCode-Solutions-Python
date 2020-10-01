class Solution:
    def solve(self, s, t):
        m = len(s)
        n = len(t)
        alpha = [0 for _ in range(26)]

        for i in range(m):
            alpha[ord(s[i]) - ord('a')] += 1

        for i in range(n):
            alpha[ord(t[i]) - ord('a')] -= 1

        for i in alpha:
            if i != 0: return False

        return True

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    u = Solution()
    print(u.solve(s, t))

from collections import Counter


class Solution:
    def minWindow(self, s, t):
        m = len(s)
        n = len(t)

        if m < n: return ''

        need = Counter(t)
        missing = len(t)
        start = 0
        end = 0
        i = 0
        for j, k in enumerate(s, 1):
            missing -= need[k] > 0
            need[k] -= 1
            if not missing:
                while need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1

                if not end or j - i <= end - start:
                    start = i
                    end = j

                need[s[i]] += 1
                i += 1
                missing += 1

        return s[start:end]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    u = Solution()
    print(u.minWindow(s, t))

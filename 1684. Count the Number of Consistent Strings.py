class Solution:
    def countConsistentStrings(self, allowed: str, words):
        words = [set(w) for w in words]
        allowed = set(allowed)
        ans = 0
        for w in words:
            flag = False
            for s in w:
                if s not in allowed:
                    flag = False
                    break
                flag = True

            if flag: ans += 1

        return ans

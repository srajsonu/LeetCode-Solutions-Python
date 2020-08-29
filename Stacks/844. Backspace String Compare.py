class Solution:
    def build(self, s):
        ans = []
        for c in s:
            if c != '#':
                ans.append(c)
            else:
                ans.pop() if ans else -1

        return ''.join(ans)

    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.build(S) == self.build(T)

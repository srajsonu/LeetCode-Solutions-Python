class Solution:
    def dfs(self, s, t):
        if not s and not t: return True

        if not s or not t: return False

        if s.val != t.val: return False

        l = self.dfs(s.left, t.left)
        r = self.dfs(s.right, t.right)
        return l and r

    def isSubtree(self, s, t) -> bool:
        return s and (self.dfs(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))

class Solution:
    def dfs(self, root):
        if not root: return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.ans += abs(l) + abs(r)
        return root.val + l + r - 1

    def distributeCoins(self, root):
        self.ans = 0
        self.dfs(root)
        return self.ans

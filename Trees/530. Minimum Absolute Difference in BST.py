class Solution:
    def dfs(self, root, low, hi):
        if not root:
            return hi - low

        l = self.dfs(root.left, low, root.val)
        r = self.dfs(root.right, root.val, hi)
        return min(l, r)

    def getMinimumDifference(self, root) -> int:
        return self.dfs(root, float('-inf'), float('inf'))

class Solution:
    def dfs(self, root, mn, mx):
        if not root:
            return True

        if root.val >= mx or root.val <= mn:
            return False

        l = self.dfs(root.left, mn, root.val)
        r = self.dfs(root.right, root.val, mx)
        return l and r

    def isValidBST(self, root):
        return self.dfs(root, float('-inf'), float('inf'))

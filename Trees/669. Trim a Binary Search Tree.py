class Solution:
    def dfs(self, root, l, r):
        if not root:
            return root

        if root.val < l:
            return self.dfs(root.right, l, r)

        if root.val > r:
            return self.dfs(root.left, l, r)

        root.left = self.dfs(root.left, l, r)
        root.right = self.dfs(root.right, l, r)
        return root

    def trimBST(self, root, L, R):
        return self.dfs(root, L, R)

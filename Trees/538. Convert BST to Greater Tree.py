class Solution:
    def dfs(self, root):
        if not root:
            return

        self.dfs(root.right)
        self.ans += root.val
        root.val = self.ans
        self.dfs(root.left)
        return root

    def convertBST(self, root):
        self.ans = 0
        return self.dfs(root)

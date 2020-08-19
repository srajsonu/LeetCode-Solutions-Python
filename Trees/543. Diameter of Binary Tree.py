class Solution:
    def dfs(self, root):
        if not root:
            return 0

        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.ans = max(self.ans, l + r + 1)
        return max(l, r) + 1

    def diameterOfBinaryTree(self, root) -> int:
        self.ans = 1
        self.dfs(root)
        return self.ans - 1

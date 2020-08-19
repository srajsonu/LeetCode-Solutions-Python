class Solution:
    def dfs(self, root):
        if not root:
            return 0

        h1 = self.dfs(root.left)
        h2 = self.dfs(root.right)

        self.ans = max(self.ans, abs(h1 - h2))

        return max(h1, h2) + 1

    def isBalanced(self, root) -> bool:
        self.ans = 0
        self.dfs(root)

        if self.ans > 1:
            return False
        return True

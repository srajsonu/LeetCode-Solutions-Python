class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root):
        if not root:
            return 0

        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.ans = max(self.ans, l + r)
        return max(l, r) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        self.dfs(root)
        return self.ans if self.ans != float('-inf') else 0

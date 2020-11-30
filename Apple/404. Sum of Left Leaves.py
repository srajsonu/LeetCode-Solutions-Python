class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root):
        if not root:
            return

        if root.left and not root.left.left and not root.left.right:
            self.ans += root.left.val

        self.dfs(root.left)
        self.dfs(root.right)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans

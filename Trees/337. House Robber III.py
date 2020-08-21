class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dp(self, root, dp):
        if not root: return 0
        if root in dp:
            return dp[root]

        val = 0
        if root.left:
            val += self.dp(root.left.left, dp) + self.dp(root.left.right, dp)

        if root.right:
            val += self.dp(root.right.left, dp) + self.dp(root.right.right, dp)

        val = max(val + root.val, self.dp(root.left, dp) + self.dp(root.right, dp))

        dp[root] = val
        return val

    def rob(self, root: TreeNode) -> int:
        dp = {}
        return self.dp(root, dp)

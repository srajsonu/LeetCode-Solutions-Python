class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, val):
        if not root:
            return val

        val.add(root.val)
        l = self.dfs(root.left, val)
        r = self.dfs(root.right, val)
        return l and r

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        val = self.dfs(root, set())
        min_ = root.val
        ans = float('inf')

        for i in val:
            if min_ < i and i < ans:
                ans = i
        return ans if ans != float('inf') else -1

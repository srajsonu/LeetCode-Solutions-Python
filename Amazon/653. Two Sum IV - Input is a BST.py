class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, k, vis):
        if not root:
            return False

        if k - root.val in vis:
            return True

        vis.add(root.val)
        l = self.dfs(root.left, k, vis)
        r = self.dfs(root.right, k, vis)
        return l or r

    def findTarget(self, root: TreeNode, k: int) -> bool:
        vis = set()
        return self.dfs(root, k, vis)

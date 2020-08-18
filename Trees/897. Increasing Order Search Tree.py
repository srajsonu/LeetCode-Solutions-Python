class TreeNode:
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root, parent):
        if not root:
            return parent

        ans = self.inorder(root.left, root)
        root.left = None
        root.right = self.inorder(root.right, parent)
        return ans

    def increasingBST(self, root):
        return self.inorder(root, None)

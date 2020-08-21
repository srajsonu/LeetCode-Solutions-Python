class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bst(self, pre, sort):
        if not pre or not sort:
            return

        node = TreeNode(pre.pop(0))
        idx = sort.index(node.val)
        node.left = self.bst(pre, sort[:idx])
        node.right = self.bst(pre, sort[idx + 1:])
        return node

    def bstFromPreorder(self, preorder) -> TreeNode:
        sort = sorted(preorder)
        return self.bst(preorder, sort)

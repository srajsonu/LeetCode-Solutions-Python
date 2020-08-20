class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, head):
        if not root and not head:
            return True

        if not head and root:
            return True

        if not root and head:
            return False

        if root.val != head.val:
            return False

        l = self.dfs(root.left, head.next)
        r = self.dfs(root.right, head.next)
        return l or r

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        return root and (self.dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right))

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, root, val):
        if not root:
            return

        if root.val == val:
            return root

        if val < root.val:
            return self.dfs(root.left, val)

        if root.val < val:
            return self.dfs(root.right, val)


if __name__ == '__main__':
    node = Node(4)
    node.left = Node(2)
    node.right = Node(7)
    node.left.left = Node(1)
    node.left.right = Node(3)
    val = 2
    A = Solution()
    print(A.dfs(node, val))

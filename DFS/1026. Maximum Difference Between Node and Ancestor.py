class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, root, mx, mn):
        if not root:
            return mx - mn

        mx = max(root.val, mx)
        mn = min(root.val, mn)

        l = self.dfs(root.left, mx, mn)
        r = self.dfs(root.right, mx, mn)
        return max(l, r)

    def Solve(self, root):
        return self.dfs(root, root.val, root.val)


if __name__ == '__main__':
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    node.right.left = Node(6)
    node.right.right = Node(7)

    A = Solution()
    print(A.Solve(node))

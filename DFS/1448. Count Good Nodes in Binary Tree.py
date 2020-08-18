from collections import deque
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root, parent):
        if not root:
            return 0

        if root.val >= parent:
            self.count += 1
            
        l = self.dfs(root.left, max(root.val, parent))
        r = self.dfs(root.right, max(root.val, parent))
        return l + r

    def Solve(self, A):
        self.count = 0
        self.dfs(A, -1)
        return self.count

if __name__ == '__main__':
    node = Node(3)
    node.left = Node(1)
    node.right = Node(4)
    node.left.left = Node(3)
    node.right.left = Node(1)
    node.right.right = Node(5)

    B = Solution()
    print(B.Solve(node))

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root):
        if not root:
            return None, 0

        l1, h1 = self.dfs(root.left)
        l2, h2 = self.dfs(root.right)

        if h1 < h2:
            return l2, h2 + 1
        elif h1 > h2:
            return l1, h1+1
        else:
            return root, h1 + 1

    def Solve(self, root):
        nodes, ht =self.dfs(root)
        print(nodes.val, nodes.left.val, nodes.right.val)

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

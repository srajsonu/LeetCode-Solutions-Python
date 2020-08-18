class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, node, sum_):
        if not node:
            return 0

        curr = sum_ * 10 + node.val
        if not node.left and not node.right:
            return curr

        l = self.dfs(node.left, curr)
        r = self.dfs(node.right, curr)
        return l + r

    def Solve(self, node,):
        return self.dfs(node, 0)


if __name__ == '__main__':
    node = Node(4)
    node.left = Node(9)
    node.right = Node(0)
    node.left.left = Node(5)
    node.left.right = Node(1)

    B = Solution()
    ans = 0
    print(B.Solve(node))
    print(ans)

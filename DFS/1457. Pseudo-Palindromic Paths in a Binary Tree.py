class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isPalindrome(self, aux):
        cnt = 0
        for i in range(10):
            if aux[i] % 2 != 0:
                cnt += 1

            if cnt > 1:
                return False
        return True

    def dfs(self, root, aux):
        if not root:
            return 0

        aux[root.val] += 1
        if not root.left and not root.right:
            if self.isPalindrome(aux):
                self.ans += 1

        self.dfs(root.left, aux)
        self.dfs(root.right, aux)

        aux[root.val] -= 1

    def Solve(self, root):
        aux = [0 for _ in range(10)]
        self.ans = 0
        self.dfs(root, aux)
        return self.ans


if __name__ == '__main__':
    node = Node(2)
    node.left = Node(3)
    node.right = Node(1)
    node.left.left = Node(3)
    node.left.right = Node(1)
    node.right.right = Node(1)

    A = Solution()
    print(A.Solve(node))

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root):
        if not root:
            return ""

        aux = str(root.val)
        l = self.dfs(root.left)
        r = self.dfs(root.right)

        if not l and not r:
            return aux

        elif not l:
            aux += '()' + '(' + r + ')'

        elif not r:
            aux += '(' + l + ')'
        else:
            aux += '(' + l + ')' + '(' + r + ')'

        return aux

    def tree2str(self, root):
        q = deque()
        q.append(root)
        ans = ""
        while q:
            node = q.pop()
            if node == ')':
                ans += ')'
                continue

            ans += '(' + str(node.val)

            if not node.left and node.right:
                ans += '()'

            if node.right:
                q.append(')')
                q.append(node.right)

            if node.left:
                q.append(')')
                q.append(node.left)



        return ans[1:]



if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    # node = TreeNode(1)

    A = Solution()
    print(A.tree2str(node))

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, s, e):
        if s >= e:
            return [None]

        ans = []
        for i in range(s, e):
            left = self.dfs(s, i)
            right = self.dfs(i+1, e)

            for l in left:
                for r in right:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    ans.append(node)
        return ans

    def Solve(self, n):
        if n == 0: return [[]]
        return self.dfs(1, n+1)



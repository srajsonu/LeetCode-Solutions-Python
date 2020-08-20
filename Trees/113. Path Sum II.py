class Solution:
    def dfs(self, root, sum, aux):
        if not root:
            return []

        if not root.left and not root.right and sum - root.val == 0:
            self.ans.append(aux + [root.val])

        l = self.dfs(root.left, sum - root.val, aux + [root.val])
        r = self.dfs(root.right, sum - root.val, aux + [root.val])
        return l and r

    def pathSum(self, root, sum: int):
        self.ans = []
        self.dfs(root, sum, [])
        return self.ans

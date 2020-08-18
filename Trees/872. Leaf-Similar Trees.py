class Solution:
    def dfs(self, root, aux):
        if not root:
            return aux

        if not root.left and not root.right:
            aux += [root.val]

        l = self.dfs(root.left, aux)
        r = self.dfs(root.right, aux)
        return l and r

    def leafSimilar(self, root1, root2) -> bool:
        aux1 = []
        aux2 = []
        self.dfs(root1, aux1)
        self.dfs(root2, aux2)
        return aux1 == aux2

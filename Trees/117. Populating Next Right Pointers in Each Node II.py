class Solution:
    def dfs(self, root):
        if not root: return

        if root.left: return root.left

        if root.right: return root.right

        return self.dfs(root.next)

    def connect(self, root):
        if not root: return

        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = self.dfs(root.next)

        if root.right:
            root.right.next = self.dfs(root.next)

        self.connect(root.right)
        self.connect(root.left)

        return root

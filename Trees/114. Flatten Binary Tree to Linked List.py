class Solution:
    def flatten(self, root) -> None:
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        tmp = root.right
        root.right = root.left
        root.left = None

        while root.right:
            root = root.right

        root.right = tmp

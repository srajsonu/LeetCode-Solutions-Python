class Solution:
    def deleteNode(self, root, key):
        if not root:
            return

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right

            tmp = root.right
            mn = tmp.val
            while tmp.left:
                tmp = tmp.left
                mn = tmp.val
            root.val = mn
            root.right = self.deleteNode(root.right, root.val)

        return root


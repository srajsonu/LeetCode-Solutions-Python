class Solution:
    def check(self, root, target):
        if not root:
            return

        if root.val == target:
            self.count += 1

        self.check(root.left, target - root.val)
        self.check(root.right, target - root.val)

    def dfs(self, root, target):
        if not root:
            return

        self.check(root, target)
        self.dfs(root.left, target)
        self.dfs(root.right, target)

    def Solve(self, root, target):
        self.count = 0
        self.dfs(root, target)


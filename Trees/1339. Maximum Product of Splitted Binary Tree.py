class Solution:
    def pdt(self, root, sm):
        if not root:
            return 0

        l = self.pdt(root.left, sm)
        r = self.pdt(root.right, sm)
        self.ans = max(self.ans, l * (sm - l), r * (sm - r))
        return l + r + root.val

    def maxProduct(self, root) -> int:
        mod = 10 ** 9 + 7
        self.ans = 0
        sm = self.pdt(root, 0)
        self.pdt(root, sm)
        return self.ans % mod

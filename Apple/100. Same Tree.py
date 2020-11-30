class Solution:
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q: return False
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, cnt):
        if not root: return 0
        cnt ^= 1 << (root.val - 1)
        ans = self.dfs(root.left, cnt) + self.dfs(root.right, cnt)

        if root.left == root.right:
            if not cnt & (cnt - 1):
                ans += 1

        return ans

    def solve(self, root):
        return self.dfs(root, 0)


if __name__ == '__main__':
    A = []
    B = Solution()
    print(B.solve(A))

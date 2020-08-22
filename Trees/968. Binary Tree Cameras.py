import enum


class state(enum.Enum):
    NO_CAMERA = 0
    HAS_CAMERA = 2
    NOT_NEEDED = 1


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root):
        if not root:
            return state.NOT_NEEDED

        l = self.dfs(root.left)
        r = self.dfs(root.right)

        if l == state.NO_CAMERA or r == state.NO_CAMERA:
            self.ans += 1
            return state.HAS_CAMERA

        elif l == state.HAS_CAMERA or r == state.HAS_CAMERA:
            return state.NOT_NEEDED
        else:
            return state.NO_CAMERA

    def minCameraCover(self, root: TreeNode) -> int:
        self.ans = 0
        if self.dfs(root) == state.NO_CAMERA: self.ans += 1
        return self.ans

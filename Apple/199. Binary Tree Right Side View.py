from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode):
        if not root: return []
        q = deque()
        q.append(root)
        ans = []
        while q:
            n = len(q)
            tmp = []
            for _ in range(n):
                node = q.popleft()
                tmp.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            ans.append(tmp[-1])

        return ans

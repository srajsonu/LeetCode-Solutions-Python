from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        q = deque()
        q.append((root, 1))

        count = 0
        while q:
            node, pos = q.popleft()
            count += 1

            if not node.left and node.right:
                return count

            if node.left:
                q.append((node.left, 2 * pos))

            if node.right:
                q.append((node.right, 2 * pos + 1))

        return count

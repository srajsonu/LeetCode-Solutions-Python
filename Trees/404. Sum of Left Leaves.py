from collections import deque


class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        if not root: return 0
        q = deque()
        q.append(root)

        ans = 0
        while q:
            node = q.popleft()

            if node.left and not node.left.left and not node.left.right:
                ans += node.left.val

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return ans

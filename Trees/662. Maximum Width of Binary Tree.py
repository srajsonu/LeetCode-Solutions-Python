from collections import deque


class Solution:
    def widthOfBinaryTree(self, root) -> int:
        q = deque()
        q.append((root, 1))
        ans = 1

        while q:
            size = len(q)
            ans = max(ans, q[-1][1] - q[0][1] + 1)
            for _ in range(size):
                node, pos = q.popleft()

                if node.left:
                    q.append((node.left, 2 * pos))

                if node.right:
                    q.append((node.right, 2 * pos + 1))

        return ans


from collections import deque


class Solution:
    def averageOfLevels(self, root):
        if not root:
            return

        q = deque()
        q.append(root)
        ans = []
        while q:
            size = len(q)
            sum_ = 0
            count = 0
            for _ in range(size):
                node = q.popleft()
                sum_ += node.val
                count += 1

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(sum_ / count)

        return ans

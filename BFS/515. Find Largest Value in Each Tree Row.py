from collections import deque


class Solution:
    def largestValues(self, root):
        if not root: return []
        q = deque()
        q.append(root)
        ans = []

        while q:
            size = len(q)
            tmp = float('-inf')
            for i in range(size):
                curr = q.popleft()
                tmp = max(tmp, curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            ans.append(tmp)

        return ans

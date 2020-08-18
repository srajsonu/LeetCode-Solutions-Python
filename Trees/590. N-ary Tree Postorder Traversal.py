from collections import deque


class Solution:
    def postorder(self, root):
        q = deque()
        if not root:
            return []
        ans = []

        q.append(root)

        while q:
            node = q.pop()
            ans.append(node.val)

            for child in node.children:
                q.append(child)

        return ans[::-1]

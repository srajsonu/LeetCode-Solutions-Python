from collections import defaultdict, deque


class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []
        q = deque()
        q.append(root)
        ans = []
        level = 1
        while q:
            tmp = deque()
            level += 1
            size = len(q)
            for _ in range(size):
                curr = q.popleft()

                if level % 2 != 0:
                    tmp.appendleft(curr.val)
                else:
                    tmp.append(curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
            ans.append(tmp)

        return ans

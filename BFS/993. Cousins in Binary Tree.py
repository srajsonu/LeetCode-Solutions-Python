from collections import deque


class Solution:
    def isCousins(self, root, x, y):
        if not root: return False
        q = deque()
        q.append(root)

        while q:
            flag1 = 0
            flag2 = 0
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if curr.val == x:
                    flag1 = 1

                if curr.val == y:
                    flag2 = 1

                # if child has same parents
                if curr.left and curr.right:
                    if curr.left.val == x and curr.right.val == y:
                        return False

                    if curr.left.val == y and curr.right.val == x:
                        return False

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            if flag1 and flag2: return True

        return False

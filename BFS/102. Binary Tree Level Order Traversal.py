from collections import defaultdict, deque

class Solution:
    def __init__(self):
        self.ans = defaultdict(list)

    def visit(self, A, level):
        if not A:
            return
        self.ans[level].append(A.val)
        self.visit(A.left, level + 1)
        self.visit(A.right, level + 1)

    def Solve(self, root):
        if root:
            self.visit(root, 0)
            return [v for v in self.ans.values()]
        return []

    #BFS
    def levelOrder(self, root):
        if not root: return []
        q = deque()
        q.append(root)
        ans = []
        while q:
            size = len(q)
            tmp = []
            for _ in range(size):
                curr = q.popleft()
                tmp.append(curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
            ans.append(tmp)
        return ans

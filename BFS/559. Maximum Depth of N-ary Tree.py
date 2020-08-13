from collections import deque, OrderedDict
class Node:
    def __init__(self, val, child):
        self.val = val
        self.child = child

class Solution:
    def Solve(self, node):
        q = deque()
        q.append(node)

        level = 0
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                for child in curr.child:
                    q.append(child)
            level += 1

        return level


if __name__ == '__main__':
    A = []
    B = Solution()
    print(B.Solve(A))

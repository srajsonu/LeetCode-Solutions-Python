from collections import deque
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Solve(self, root):
        q = deque()
        q.append(root)
        ans = []
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left:
                    if node.left.left:
                        if node.val % 2 == 0:
                            ans.append(node.left.left.val)
                    if node.left.right:
                        if node.val % 2 == 0:
                            ans.append(node.left.right.val)
                    q.append(node.left)

                if node.right:
                    if node.right.left:
                        if node.val % 2 == 0:
                            ans.append(node.right.left.val)
                    if node.right.right:
                        if node.val % 2 == 0:
                            ans.append(node.right.right.val)
                    q.append(node.right)

        return sum(ans)

if __name__ == '__main__':
    node = Node(6)
    node.left = Node(7)
    node.right = Node(8)
    node.left.left = Node(2)
    node.left.right = Node(7)
    node.left.left.left = Node(9)
    node.left.right.left = Node(1)
    node.left.right.right = Node(4)
    node.right.left = Node(1)
    node.right.right = Node(3)
    node.right.right.right = Node(5)

    A = Solution()
    print(A.Solve(node))





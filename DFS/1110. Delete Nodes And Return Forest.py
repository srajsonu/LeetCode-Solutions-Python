from collections import deque
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Solve(self, root, nodes):
        nodes = set(nodes)
        q = deque()
        q.append((root, False))
        ans = []
        while q:
            node, hasParent = q.popleft()

            if node.val not in nodes and not hasParent:
                ans.append(node)

            hasParent = not node.val in nodes

            if node.left:
                q.append((node.left, hasParent))
                if node.left.val in nodes:
                    node.left = None

            if node.right:
                q.append((node.right, hasParent))
                if node.right.val in nodes:
                    node.right = None

        return ans


if __name__ == '__main__':
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    node.right.left = Node(6)
    node.right.right = Node(7)
    nodes = [3,5]

    B = Solution()
    print(B.Solve(node, nodes))

from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def build(self, root, parent):
        if root and parent:
            self.graph[root].append(parent)
            self.graph[parent].append(root)

        if root.left:
            self.build(root.left, root)

        if root.right:
            self.build(root.right, root)

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.graph = defaultdict(list)
        self.build(root, None)

        vis = set()
        q = deque()
        q.append((target, 0))
        # vis.add(target)

        ans = []
        while q:
            size = len(q)
            for _ in range(size):
                node, pos = q.popleft()
                vis.add(node)

                if pos == K:
                    ans.append(node.val)

                for elem in self.graph[node]:
                    if elem not in vis:
                        print(node.val, pos)
                        vis.add(elem)
                        q.append((elem, pos + 1))
        return ans

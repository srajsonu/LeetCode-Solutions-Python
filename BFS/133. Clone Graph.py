from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def __init__(self):
        self.vis = {}

    def cloneGraph(self, node):
        if not node:
            return None

        if node in self.vis:
            return self.vis[node]

        new_node = Node(node.val)
        self.vis[node] = new_node
        new_node.neighbors = []

        for child in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(child))

        return new_node

    def bfs(self, node):
        if not node:
            return

        q = deque()
        q.append(node)
        vis = {}
        vis[node] = Node(node.val)

        while q:
            root = q.popleft()
            for child in root.neighbors:
                if child not in vis:
                    vis[child] = Node(child.val)
                    q.append(child)
                vis[root].neighbors.append(vis[child])

        return vis[node]



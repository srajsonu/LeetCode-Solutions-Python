from collections import defaultdict


class Solution:
    def dfs(self, v, vis):
        vis.add(v)

        for w in self.graph[v]:
            if w not in vis:
                vis.add(w)
                self.dfs(w, vis)

    def canVisitAllRooms(self, rooms):
        m = len(rooms)
        self.graph = defaultdict(list)

        for i in range(m):
            for j in range(len(rooms[i])):
                self.graph[i].append(rooms[i][j])

        vis = set()
        self.dfs(0, vis)
        return len(vis) == m

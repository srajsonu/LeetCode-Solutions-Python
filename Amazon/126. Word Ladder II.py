from collections import deque, defaultdict


class Solution:
    def bfs(self, A, B, C):
        C = set(C)
        q = deque()
        q.append((A, 0))
        vis = {}
        vis[A] = 0
        while q:
            word, depth = q.popleft()
            parent = word
            if word == B:
                return depth + 1

            word = [i for i in word]
            for i in range(len(word)):
                tmp = word[i]
                for j in range(ord('a'), ord('z') + 1):
                    if tmp == chr(j):
                        continue

                    word[i] = chr(j)
                    new_word = ''.join(word)
                    if new_word in C:
                        if new_word not in vis:
                            self.graph[parent].append(new_word)
                            vis[new_word] = vis[parent] + 1
                            q.append((new_word, depth + 1))
                        elif vis[new_word] == vis[parent] + 1:
                            self.graph[parent].append(new_word)

                word[i] = tmp

        return 0

    def dfs(self, s, e, path):
        path.append(s)
        if s == e:
            self.ans.append(path[:])
            path.pop()
            return

        for v in self.graph[s]:
            self.dfs(v, e, path)

        path.pop()

    def findLadders(self, A, B, C):
        self.graph = defaultdict(list)
        self.bfs(A, B, C)
        self.ans = []
        path = []
        self.dfs(A, B, path)
        return self.ans


if __name__ == '__main__':
    A = "hit"
    B = "cog"
    C = ["hot","dot","dog","lot","log","cog"]
    D = Solution()
    print(D.findLadders(A, B, C))

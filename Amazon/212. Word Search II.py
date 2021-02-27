class TrieNode:
    def __init__(self):
        self.child = {}
        self.terminal = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, w):
        head = self.root
        for i in w:
            if i in head.child:
                head = head.child[i]
            else:
                head.child[i] = TrieNode()
                head = head.child[i]
        head.terminal = True
        head.word = w


class Solution:
    def dfs(self, A, head, i, j):
        if head.word:
            self.ans.append(head.word)
            head.word = None

        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return

        tmp = A[i][j]
        head = head.child.get(tmp)

        if not head:
            return

        row = [-1, 0, 1, 0]
        col = [0, -1, 0, 1]

        A[i][j] = ''

        for r, c in zip(row, col):
            nRow = i + r
            nCol = j + c
            self.dfs(A, head, nRow, nCol)

        A[i][j] = tmp

    def findWords(self, A, B):
        trie = Trie()
        for w in B:
            trie.insert(w)

        self.ans = []
        m = len(A)
        n = len(A[0])

        node = trie.root
        for i in range(m):
            for j in range(n):
                self.dfs(A, node, i, j)

        return self.ans


if __name__ == '__main__':
    A = [["o", "a", "a", "n"],
         ["e", "t", "a", "e"],
         ["i", "h", "k", "r"],
         ["i", "f", "l", "v"]]
    B = ["oath", "pea", "eat", "rain"]
    C = Solution()
    print(C.findWords(A, B))

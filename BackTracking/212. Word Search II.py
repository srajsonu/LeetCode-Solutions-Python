class TrieNode:
    def __init__(self):
        self.child = {}
        self.terminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        n = len(word)
        head = self.root
        for i in range(n):
            if word[i] in head.child:
                head = head.child[word[i]]
            else:
                head.child[word[i]] = TrieNode()
                head = head.child[word[i]]
        head.terminal = True

    def search(self,word):
        n = len(word)
        head = self.root
        for i in range(n):
            if word[i] not in head.child:
                return False
            head = head.child[word[i]]
        return True if head.terminal else False

class Solution:
    def backtrack(self,board,node,i,j, aux):
        if node.terminal:
            print(aux)
            self.ans.append(aux)
            node.terminal = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        tmp = board[i][j]
        node = node.child.get(tmp)

        if not node:
            return

        row = [1,0,-1,0]
        col = [0,1,0,-1]

        board[i][j] = '#'

        for r,c in zip(row,col):
            self.backtrack(board,node,i+r,j+c,aux + tmp)
        board[i][j] = tmp

    def findWords(self,board, words):
        m = len(board)
        n = len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)

        node = trie.root

        self.ans = []
        for i in range(m):
            for j in range(n):
                self.backtrack(board,node ,i,j,"")

        return self.ans

if __name__ == '__main__':
    board = [['o', 'a', 'a', 'n'],
             ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'],
             ['i', 'f', 'l', 'v']]

    words = ["oath", "pea", "eat", "rain"]
    C = Solution()
    print(C.findWords(board, words))

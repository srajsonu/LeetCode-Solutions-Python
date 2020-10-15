class TrieNode:
    def __init__(self):
        self.child = {}
        self.terminal = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, w: str) -> None:
        n = len(w)
        head = self.root

        for i in range(n):
            if w[i] in head.child:
                head = head.child[w[i]]
            else:
                head.child[w[i]] = TrieNode()
                head = head.child[w[i]]
        head.terminal = True

    def search(self, w: str) -> bool:
        n = len(w)
        head = self.root

        for i in range(n):
            if w[i] not in head.child:
                return False

            head = head.child[w[i]]

        return True if head.terminal else False

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for s in prefix:
            if s not in head.child:
                return False
            head = head.child[s]

        return True

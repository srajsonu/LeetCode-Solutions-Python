class TrieNode:
    def __init__(self):
        self.child = {}
        self.cnt = 0
        self.terminal = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, w):
        n = len(w)
        head = self.root
        for i in range(n):
            if w[i] in head.child:
                head = head.child[w[i]]
                head.cnt += 1
            else:
                head.child[w[i]] = TrieNode()
                head = head.child[w[i]]
                head.cnt = 1

        head.terminal = True


class Solution:
    def longestCommonPrefix(self, strs):
        trie = Trie()
        for w in strs:
            trie.insert(w)
        global ans
        for w in strs:
            head = trie.root
            tmp = ""
            for i in w:
                if head.child[i].cnt == len(strs):
                    tmp += i
                head = head.child[i]
            ans = tmp

        return ans

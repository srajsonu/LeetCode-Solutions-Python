class TrieNode:
    def __init__(self):
        self.child = {}
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
            else:
                head.child[w[i]] = TrieNode()
                head = head.child[w[i]]

        head.terminal = True

    def search(self, w):
        n = len(w)
        head = self.root

        for i in range(n):
            if w[i] not in head.child:
                return False

            head = head.child[w[i]]

        return True if head.terminal else False


class Solution:
    def wordBreak(self, s, dic):
        n = len(s)
        trie = Trie()
        for i in dic:
            trie.insert(i)

        dp = [False for _ in range(n+1)]
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and trie.search(s[j:i]):
                    dp[i] = True
                    break

        return dp[-1]


if __name__ == '__main__':
    s = 'leetcode'
    dic = ["leet", "code"]
    t = Solution()
    print(t.wordBreak(s, dic))

class TrieNode:
    def __init__(self):
        self.child = {}
        self.terminal = False

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

    def search(self, w):
        head = self.root

        for i in w:
            if i not in head.child:
                return False
            head = head.child[i]

        return True if head.terminal else False

class Solution:
    def wordBreak(self, A, B):
        trie = Trie()
        for w in B:
            trie.insert(w)

        n = len(A)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and trie.search(A[j:i]):
                    dp[i] = True
                    break

        return dp[-1]


if __name__ == '__main__':
    A = "leetcode"
    B = ["leet", "code"]
    C = Solution()
    print(C.wordBreak(A, B))

class Solution:
    def match(self, word):
        m1 = {}
        m2 = {}

        for w, p in zip(word, self.p):
            if w not in m1:
                m1[w] = p

            if p not in m2:
                m2[p] = w

            if (m1[w], m2[p]) != (p, w):
                return False

        return True

    def solve(self, A, B):
        self.p = B
        val = filter(self.match, A)
        ans = []
        for i in val:
            ans.append(i)

        return ans



if __name__ == '__main__':
    A = ["abc","deq","mee","aqq","dkd","ccc"]
    B = 'abb'
    C = Solution()
    print(C.solve(A, B))

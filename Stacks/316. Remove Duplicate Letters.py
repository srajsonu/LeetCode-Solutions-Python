class Solution:
    def solve(self, A):
        freq = {}
        for i in A:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        ans = []
        vis = set()

        for i in A:
            freq[i] -= 1
            if i in vis:
                continue

            while ans and ans[-1] > i and freq[ans[-1]] > 0:
                vis.remove(ans.pop())

            ans.append(i)
            vis.add(i)

        return ''.join(ans)

if __name__ == '__main__':
    A = "cbacdcbc"
    B = Solution()
    print(B.solve(A))

class Solution:
    def sort(self, enum, nums):
        n = len(enum)
        mid = n // 2

        if mid:
            l = self.sort(enum[:mid], nums)
            r = self.sort(enum[mid:], nums)

            for i in reversed(range(n)):
                if not r or l and l[-1][1] > r[-1][1]:
                    self.ans[l[-1][0]] += len(r)
                    enum[i] = l.pop()
                else:
                    enum[i] = r.pop()

        return enum

    def countSmaller(self, arr):
        n = len(arr)
        self.ans = [0 for _ in range(n)]
        self.sort(list(enumerate(arr)), arr)
        return self.ans


if __name__ == '__main__':
    arr = [5, 2, 6, 1]
    A = Solution()
    print(A.countSmaller(arr))

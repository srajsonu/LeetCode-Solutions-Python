from collections import defaultdict


class Solution:
    def __init__(self):
        self.freq = {}
        self.stack_freq = defaultdict(list)
        self.max_freq = 0

    def push(self, x):
        if x not in self.freq:
            self.freq[x] = 1
        else:
            self.freq[x] += 1

        self.stack_freq[self.freq[x]].append(x)
        self.max_freq = max(self.max_freq, self.freq[x])

    def pop(self):
        ans = self.stack_freq[self.max_freq].pop()
        self.freq[ans] -= 1
        if not self.stack_freq[self.max_freq]:
            self.max_freq -= 1
        return ans

    def solve(self, A):
        for x in A:
            self.push(x)


if __name__ == '__main__':
    A = [5, 7, 5, 7, 4, 5]
    B = Solution()
    print(B.solve(A))

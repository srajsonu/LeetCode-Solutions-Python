from collections import defaultdict
from typing import List


class Solution:
    def find_root(self, A, parent):
        if parent[A] == A:
            return A
        return self.find_root(parent[A], parent)

    def union(self, A, B, parent, height):
        C = self.find_root(A, parent)
        D = self.find_root(B, parent)

        if C == D:
            return

        if height[C] < height[D]:
            parent[C] = D
        elif height[C] > height[D]:
            parent[D] = C
        else:
            parent[D] = C
            height[C] += 1

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        parent = [i for i in range(n)]
        height = [0 for _ in range(n)]

        graph = defaultdict(list)
        ans = []

        for i in range(n):
            for j in range(i + 1, n):
                tmp = self.gcd(A[i], A[j])
                print(tmp)
                if tmp != 1:
                    ans.append(tmp)
        return len(ans)



from collections import deque
class Solution:
    def combinations(self, start):
        ans = []
        states = [-1, 1]

        for i,j in enumerate(start):
            for state in states:
                val = (int(j) + state) % 10
                ans.append(start[:i] + str(val) + start[i+1:])

        return ans


    def Solve(self,A,B):
        start = '0000'
        q = deque()
        A = set(A)
        q.append((start, 0))
        vis = set()
        vis.add(start)

        while q:
            comb , level = q.popleft()

            if comb == B:
                return level

            if comb in A:
                continue

            for combination in self.combinations(comb):
                if combination not in vis:
                    vis.add(combination)
                    q.append((combination, level+1))

        return -1



if __name__ == '__main__':
    A = ["0201", "0101", "0102", "1212", "2002"]
    B = "0202"
    C = Solution()
    print(C.Solve(A,B))

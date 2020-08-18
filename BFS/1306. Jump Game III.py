from collections import deque


class Solution:
    def isValid(self, A, i):
        if i < 0 or i >= len(A):
            return False
        return True

    def Solve(self, A, B):
        n = len(A)
        q = deque()
        q.append(B)
        vis = [False for _ in range(n)]

        while q:
            i = q.popleft()
            vis[i] = True
            if self.isValid(A, i + A[i]) and not vis[i + A[i]]:
                vis[i + A[i]] = True
                q.append(i + A[i])

            if self.isValid(A, i - A[i]) and not vis[i - A[i]]:
                vis[i - A[i]] = True
                q.append(i - A[i])
            if A[i] == 0:
                return True

        return False


if __name__ == '__main__':
    A = [3,0,2,1,2]
    B = 2
    C = Solution()
    print(C.Solve(A, B))

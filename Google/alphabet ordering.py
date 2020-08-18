class Solution:
    def dp(self, A, index, prev,  state, aux):
        if index == len(A):
            return max(self.inc, self.dec)

        for i in range(index, len(A)):
            # if ord(prev) < ord(A[i]):
            #     aux += A[i]
            #     self.inc += 1
            # else:
            #     aux.pop()
            #     aux += A[i]
            #     self.dec += 1
            print(aux)

            self.dp(A, index+1 , A[i], True, aux + A[i])

    def Solve(self, s, maps):
        self.inc = 0
        self.dec = 0
        return self.dp(A, 0,"", False, "")


if __name__ == '__main__':
    A = 'gfcbdhdd'
    B ={'cat', 'map', 'bat', 'man', 'pen'}
    C = Solution()
    print(C.Solve(A, B))

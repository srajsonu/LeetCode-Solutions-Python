class Solution:
    def maximumWealth(self, A):
        m = len(A)
        n = len(A[0])

        ans = float('-inf')
        for i in range(m):
            amt = 0
            for j in range(n):
                amt += A[i][j]
            ans = max(ans, amt)

        return ans

if __name__ == '__main__':
    A = [[1,2,3],
         [3,2,1]]

    B = Solution()
    print(B.maximumWealth(A))

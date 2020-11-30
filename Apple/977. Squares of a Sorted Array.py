class Solution:
    def sortedSquares(self, A):
        return sorted(i * i for i in A)



if __name__ == '__main__':
    A = [-4,-1,0,3,10]
    B = Solution()
    print(B.sortedSquares(A))

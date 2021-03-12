class Solution:
    def rotate(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(i):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

        for i in range(n):
            arr[i] = arr[i][::-1]

        return arr

if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    B = Solution()
    print(B.rotate(A))

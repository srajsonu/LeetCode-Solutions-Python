class Solution:
    def solve(self, arr):
        n = len(arr)
        arr.sort(key=lambda k: k[1])
        cnt = 0
        i = 0
        j = 1
        while j < n:
            if arr[i][1] > arr[j][0]:
                cnt += 1
            else:
                i = j
            j += 1

        return cnt


if __name__ == '__main__':
    A = [[0,2],[1,3],[2,4],[3,5],[4,6]]
    B = Solution()
    print(B.solve(A))

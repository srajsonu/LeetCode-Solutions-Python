class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        n = len(arr)
        cnt = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        cnt += 1

        return cnt

if __name__ == '__main__':
    A = [3, 0, 1, 1, 9, 7]
    B = 7
    C = 2
    D = 3
    E = Solution()
    print(E.countGoodTriplets(A, B, C, D))

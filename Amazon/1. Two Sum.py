class Solution:
    def twoSum(self, A, B):
        n = len(A)
        freq = {}

        for i in range(n):
            req = B - A[i]
            if req not in freq:
                freq[A[i]] = i
            else:
                return [i, freq[req]]

        return [-1, -1]


if __name__ == '__main__':
    A = [2, 7, 11, 15]
    B = 9
    C = Solution()
    print(C.twoSum(A, B))

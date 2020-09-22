class Solution:
    def twoSum(self, A, target):
        freq = {}
        for i, j in enumerate(A):
            val = target - j
            if val not in freq:
                freq[j] = i
            else:
                return [i, freq[val]]

if __name__ == '__main__':
    A = [2,7,11,15]
    target = 9
    B = Solution()
    print(B.twoSum(A, target))

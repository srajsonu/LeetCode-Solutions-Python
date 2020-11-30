from collections import Counter

class Solution:
    def subarraySum(self, A, k):
        total = 0
        cnt = 0
        Hash = Counter()
        Hash[0] = 1

        for i in A:
            total += i
            cnt += Hash[total-k]
            Hash[total] += 1

        return cnt




if __name__ == '__main__':
    A = [1, 2, 3]
    B = 3
    C = Solution()
    print(C.subarraySum(A, B))

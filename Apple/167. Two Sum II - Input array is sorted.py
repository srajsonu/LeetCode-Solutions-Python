class Solution:
    def twoSum(self, num, target):
        Hash = {}
        ans = []
        for i, j in enumerate(num):
            val = target-j
            if val in Hash:
                ans += [Hash[val]+1, i+1]
            Hash[j] = i

        return ans

    def two_pointer(self, num, target):
        l = 0
        r = len(num) - 1
        while l <= r:
            if num[l] + num[r] == target:
                return [l + 1, r + 1]

            elif num[l] + num[r] < target:
                l += 1

            else:
                r -= 1

        return []

    def binarySearch(self, num, target):
        n = len(num)
        for i in range(n):
            l, r = i+1, n-1
            val = target - num[i]

            while l <= r:
                mid = (l+r) // 2
                if num[mid] == val:
                    return [i+1, mid+1]
                elif num[mid] < val:
                    l = mid+1
                else:
                    r = mid-1

        return []



if __name__ == '__main__':
    A = [2,7,11,15]
    B = 9
    C = Solution()
    print(C.twoSum(A, B))
    print(C.two_pointer(A, B))
    print(C.binarySearch(A, B))

class Solution:
    def rotation(self, A, l, h):
        n = len(A)
        mid = (l + h) // 2

        if A[mid] > A[mid + 1]:
            return mid

        elif A[mid] > A[n - 1]:
            return self.rotation(A, mid + 1, h)
        else:
            return self.rotation(A, l, mid - 1)

    def find(self, A, target, l, h, k):
        n = len(A)
        mid = (l + h) // 2
        if l > h: return -1

        if A[(mid + k) % n] == target:
            return (mid + k) % n

        if A[(mid + k) % n] > target:
            return self.find(A, target, l, mid - 1, k)
        else:
            return self.find(A, target, mid + 1, h, k)

    def search(self, nums, target):
        n = len(nums)
        if n == 1:
            if target != nums[0]:
                return -1
            else:
                return 0

        k = self.rotation(nums, 0, n - 1)
        return self.find(nums, target, 0, n - 1, k + 1)

if __name__ == '__main__':
    A = [4, 5, 6, 7, 0, 1, 2]
    B = 0
    C = Solution()
    print(C.search(A, B))

class Solution:
    def findDisappearedNumbers(self, arr):
        if not arr: return []
        n = len(arr)
        arr = set(arr)
        ans = []
        for i in range(1, n+1):
            if i not in arr:
                ans.append(i)

        return ans

if __name__ == '__main__':
    A = [4,3,2,7,8,2,3,1]
    B = Solution()
    print(B.findDisappearedNumbers(A))

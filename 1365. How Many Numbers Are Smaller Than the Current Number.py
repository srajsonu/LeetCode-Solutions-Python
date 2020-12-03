class Solution:
    def smallerNumbersThanCurrent(self, A):
        ans = {}
        for i, j in enumerate(sorted(A)):
            if j not in ans:
                ans[j] = i

        return [ans[num] for num in A]

if __name__ == '__main__':
    A = [8, 1, 2, 2, 3] #[4, 0, 1, 1, 3]
    B = Solution()
    print(B.smallerNumbersThanCurrent(A))

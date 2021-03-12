class Solution:
    def threeSum(self, A):
        n = len(A)
        A.sort()
        ans = []
        for i in range(n):
            if i > 0 and A[i] == A[i-1]:
                continue

            a = A[i]
            l = i+1
            h = n-1

            while l < h:
                b = A[l]
                c = A[h]
                sm = a + b + c
                if sm == 0:
                    ans.append([a, b, c])
                    l += 1
                    while l < h and A[l] == A[l-1]:
                        l += 1

                elif sm < 0:
                    l += 1
                else:
                    h -= 1

        return ans



if __name__ == '__main__':
    A = [-2,0,1,1,2]
    B = Solution()
    print(B.threeSum(A))

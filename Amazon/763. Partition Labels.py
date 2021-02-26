from collections import OrderedDict


class Solution:
    def partitionLabels(self, A):
        n = len(A)
        freq = OrderedDict()

        for i in A:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        ans = []
        k = 0
        for i in range(n):
            freq[A[i]] -= 1

            if freq[A[i]] == 0:
                cnt = 0
                tmp = 0
                j = k
                while j <= i:
                    if freq[A[j]] == 0:
                        cnt += 1
                    else:
                        j = i+1
                        cnt = 0
                        break
                    j += 1

                if tmp < cnt:
                    tmp = cnt
                    k = j
                    ans.append(tmp)

        return ans

if __name__ == '__main__':
    A = "ababcbacadefegdehijhklij"
    B = Solution()
    print(B.partitionLabels(A))

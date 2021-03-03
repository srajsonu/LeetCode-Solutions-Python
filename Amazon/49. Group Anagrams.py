from collections import defaultdict


class Solution:
    def groupAnagrams(self, A):
        ans = defaultdict(list)

        for i in A:
            tmp = sorted(i)
            ans[''.join(tmp)].append(i)

        return ans.values()

if __name__ == '__main__':
    A = ["eat", "tea", "tan", "ate", "nat", "bat"]
    B = Solution()
    print(B.groupAnagrams(A))

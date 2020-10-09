from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(list)

        for s in strs:
            ans[tuple(sorted(s))].append(s)

        return ans.values()

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    A = Solution()
    print(A.groupAnagrams(strs))

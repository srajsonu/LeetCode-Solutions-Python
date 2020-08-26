class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        pre = [0 for _ in range(n)]
        pre_set = set()

        suf = [0 for _ in range(n)]
        suf_set = set()

        for i in range(n):
            pre_set.add(s[i])
            suf_set.add(s[n - i - 1])
            pre[i] = len(pre_set)
            suf[n - i - 1] = len(suf_set)

        cnt = 0
        for i in range(1, n):
            if pre[i - 1] == suf[i]:
                cnt += 1

        return cnt

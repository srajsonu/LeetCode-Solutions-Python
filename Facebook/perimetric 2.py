class Solution:
    def pdt(self, A):
        mod = 10 ** 9 + 7
        ans = 1
        for i in A:
            ans *= (i%mod)
            ans %= mod
        return ans % mod

    def Solve(self, L, H, N, K, W):
        i = K
        while i < N:
            L.append(((Al * L[i - 2] + Bl * L[i - 1] + Cl) % Dl) + 1)
            W.append(((Aw * W[i - 2] + Bw * W[i - 1] + Cw) % Dw) + 1)
            H.append(((Ah * H[i - 2] + Bh * H[i - 1] + Ch) % Dh) + 1)
            i += 1

        mod = 10 ** 9 + 7
        n = len(L)
        ans = [2 * (W[0] + H[0])]
        prevP = ans[0]
        prevL = L[0]
        prevH = H[0]
        prevW = W[0]
        periN = 0
        for i in range(1, n):
            if L[i] <= L[i - 1] + W[i-1] and L[i] + W[i] >= L[i-1]:
                height = max(H[i], prevH)
                width = L[i] + W[i] - prevL
                prevW += W[i]
                peri = 2 * (height + prevW) + periN
                prevP = peri
                prevH = height
                ans.append(peri)
            else:
                periN = prevP
                prevP += 2 * (H[i] + W[i])
                prevL = L[i]
                prevH = H[i]
                prevW = W[i]
                ans.append(prevP)
                prevP = periN

            # if L[i] < L[i-1]:
            #     peri += 2 * (H[i] + W) - (2 * (abs(L[i] - L[i-1]) + max(H[i], H[i-1])))
            # else:
            #     peri += 2 * (H[i] + W)
            #
            # L[i] += W
            # ans.append(perim)

        return self.pdt(ans), ans


if __name__ == '__main__':
    A = Solution()
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        L = list(map(int, input().split()))
        Al, Bl, Cl, Dl = map(int, input().split())
        W = list(map(int, input().split()))
        Aw, Bw, Cw, Dw = map(int, input().split())
        H = list(map(int, input().split()))
        Ah, Bh, Ch, Dh = map(int, input().split())
        print("Case #" + str(i + 1) + ":", A.Solve(L, H, N, K, W))

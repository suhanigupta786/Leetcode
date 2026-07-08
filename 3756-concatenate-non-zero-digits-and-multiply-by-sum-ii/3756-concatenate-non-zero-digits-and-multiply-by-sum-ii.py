class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        pos = []
        digit = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digit.append(int(ch))

        m = len(pos)

        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        pref_num = [0] * (m + 1)
        pref_sum = [0] * (m + 1)

        for i in range(m):
            pref_num[i + 1] = (pref_num[i] * 10 + digit[i]) % MOD
            pref_sum[i + 1] = pref_sum[i] + digit[i]

        def lower_bound(x):
            lo, hi = 0, m
            while lo < hi:
                mid = (lo + hi) // 2
                if pos[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def upper_bound(x):
            lo, hi = 0, m
            while lo < hi:
                mid = (lo + hi) // 2
                if pos[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        ans = []

        for l, r in queries:
            L = lower_bound(l)
            R = upper_bound(r)

            if L == R:
                ans.append(0)
                continue

            length = R - L

            num = (pref_num[R] - pref_num[L] * pow10[length]) % MOD
            sm = pref_sum[R] - pref_sum[L]

            ans.append((num * sm) % MOD)

        return ans
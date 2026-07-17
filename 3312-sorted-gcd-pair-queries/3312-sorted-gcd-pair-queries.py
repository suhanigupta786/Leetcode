class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        divCnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for m in range(g, mx + 1, g):
                divCnt[g] += freq[m]

        exact = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            c = divCnt[g]
            pairs = c * (c - 1) // 2

            m = 2 * g
            while m <= mx:
                pairs -= exact[m]
                m += g

            exact[g] = pairs

        pref = [0] * (mx + 1)
        for g in range(1, mx + 1):
            pref[g] = pref[g - 1] + exact[g]

        ans = []

        for k in queries:
            k += 1

            lo, hi = 1, mx
            while lo < hi:
                mid = (lo + hi) // 2
                if pref[mid] >= k:
                    hi = mid
                else:
                    lo = mid + 1

            ans.append(lo)

        return ans
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left = 0
        right = max(diff)

        while left < right:
            mid = (left + right) // 2
            need = 0

            for x in diff:
                if x > mid:
                    need += x - mid

            if need <= k:
                right = mid
            else:
                left = mid + 1

        ans = 0

        for x in diff:
            reduced = min(x, left)
            k -= max(0, x - left)
            ans += reduced * reduced

        for i in range(len(diff)):
            if k == 0:
                break
            if diff[i] >= left:
                ans -= left * left - (left - 1) * (left - 1)
                k -= 1

        return ans
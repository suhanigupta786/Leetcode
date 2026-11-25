class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        mod1 = 10**9 + 7
        mod2 = 10**9 + 9
        base = 911382323

        power1 = [1] * (n + 1)
        power2 = [1] * (n + 1)

        prefix1 = [0] * (n + 1)
        prefix2 = [0] * (n + 1)

        for i in range(n):
            power1[i + 1] = power1[i] * base % mod1
            power2[i + 1] = power2[i] * base % mod2

            prefix1[i + 1] = (prefix1[i] * base + nums[i]) % mod1
            prefix2[i + 1] = (prefix2[i] * base + nums[i]) % mod2

        def check(k):
            count = {}

            for i in range(n - k + 1):
                h1 = (prefix1[i + k] - prefix1[i] * power1[k]) % mod1
                h2 = (prefix2[i + k] - prefix2[i] * power2[k]) % mod2

                key = (h1, h2)
                count[key] = count.get(key, 0) + 1

            for value in count.values():
                if value == 1:
                    return True

            return False

        left = 1
        right = n
        ans = n

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

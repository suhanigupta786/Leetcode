class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        total = nums[0]

        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break
        seen = set(nums)

        while total in seen:
            total += 1

        return total
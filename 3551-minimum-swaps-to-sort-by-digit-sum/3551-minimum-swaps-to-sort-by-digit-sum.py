class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        def digit_sum(x):
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
            return total

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))

        pos = {}
        for i in range(n):
            pos[arr[i]] = i

        visited = [False] * n
        ans = 0

        for i in range(n):
            if visited[i] or pos[nums[i]] == i:
                continue

            j = i
            count = 0

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                count += 1

            ans += count - 1

        return ans
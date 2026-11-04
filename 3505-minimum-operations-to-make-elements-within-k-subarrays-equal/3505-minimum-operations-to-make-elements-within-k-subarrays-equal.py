
import heapq

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        small = []
        large = []
        delayed = {}

        small_size = [0]
        large_size = [0]

        small_sum = [0]
        large_sum = [0]

        def prune(heap, is_small):
            while heap:
                if is_small:
                    num = -heap[0]
                else:
                    num = heap[0]

                if num not in delayed:
                    break

                heapq.heappop(heap)
                delayed[num] -= 1

                if delayed[num] == 0:
                    del delayed[num]

        def balance():
            prune(small, True)
            prune(large, False)

            while small_size[0] > large_size[0] + 1:
                num = -heapq.heappop(small)
                small_size[0] -= 1
                small_sum[0] -= num

                heapq.heappush(large, num)
                large_size[0] += 1
                large_sum[0] += num

                prune(small, True)

            while small_size[0] < large_size[0]:
                num = heapq.heappop(large)
                large_size[0] -= 1
                large_sum[0] -= num

                heapq.heappush(small, -num)
                small_size[0] += 1
                small_sum[0] += num

                prune(large, False)

        def add(num):
            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size[0] += 1
                small_sum[0] += num
            else:
                heapq.heappush(large, num)
                large_size[0] += 1
                large_sum[0] += num

            balance()

        def remove(num):
            if num <= -small[0]:
                small_size[0] -= 1
                small_sum[0] -= num

                if num == -small[0]:
                    prune(small, True)
            else:
                large_size[0] -= 1
                large_sum[0] -= num

                if large and num == large[0]:
                    prune(large, False)

            delayed[num] = delayed.get(num, 0) + 1

            balance()

        def get_cost():
            median = -small[0]

            return (median * small_size[0] - small_sum[0]
                    + large_sum[0] - median * large_size[0])

        costs = []

        maritovexi = (nums, x, k)

        for i in range(x):
            add(nums[i])

        costs.append(get_cost())

        for i in range(x, n):
            remove(nums[i - x])
            add(nums[i])
            costs.append(get_cost())

        dp = [[float('inf')] * (k + 1) for i in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j]

                if i >= x:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - x][j - 1] + costs[i - x]
                    )

        return dp[n][k]

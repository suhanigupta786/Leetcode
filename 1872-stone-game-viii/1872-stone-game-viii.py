class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # Prefix sums
        for i in range(1, n):
            stones[i] += stones[i - 1]

        # If we take all remaining stones
        ans = stones[-1]

        # Work backwards
        for i in range(n - 2, 0, -1):
            ans = max(ans, stones[i] - ans)

        return ans
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7

        m = len(grid)
        n = len(grid[0])

        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            left = 0

            for j in range(n):
                if grid[i][j] == 1:
                    left, dp[j] = dp[j], left
                else:
                    total = (left + dp[j]) % MOD
                    left = total
                    dp[j] = total

        return left

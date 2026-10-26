class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            total = grid[i][j]
            grid[i][j] = 0

            if i > 0 and grid[i - 1][j] > 0:
                total += dfs(i - 1, j)

            if i < m - 1 and grid[i + 1][j] > 0:
                total += dfs(i + 1, j)

            if j > 0 and grid[i][j - 1] > 0:
                total += dfs(i, j - 1)

            if j < n - 1 and grid[i][j + 1] > 0:
                total += dfs(i, j + 1)

            return total

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    total = dfs(i, j)

                    if total % k == 0:
                        ans += 1

        return ans
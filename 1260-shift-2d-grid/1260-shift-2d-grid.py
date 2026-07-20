class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k %= total
        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                index = i * n + j
                new_index = (index + k) % total

                new_i = new_index // n
                new_j = new_index % n

                ans[new_i][new_j] = grid[i][j]

        return ans
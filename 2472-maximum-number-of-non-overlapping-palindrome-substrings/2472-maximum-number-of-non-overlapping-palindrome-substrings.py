class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        pal = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                pal[i][j] = s[i] == s[j] and pal[i + 1][j - 1]

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]

            for j in range(i + k - 1, n):
                if pal[i][j]:
                    dp[i] = max(dp[i], 1 + dp[j + 1])

        return dp[0]
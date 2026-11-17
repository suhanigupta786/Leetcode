class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = length

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for offset in range(d):
                        left = i + offset
                        right = j - d + 1 + offset

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[i][j] = best

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for parts in range(1, k + 1):
                for j in range(i - 1):
                    if i - j < 2:
                        continue

                    dp[i][parts] = min(
                        dp[i][parts],
                        dp[j][parts - 1] + cost[j][i - 1]
                    )

        return dp[n][k]

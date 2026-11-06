
class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda a: a[1])

        sorted_queries = []
        for i in range(len(queries)):
            sorted_queries.append([queries[i], i])

        sorted_queries.sort()

        count = {}
        ans = [0] * len(queries)

        left = 0
        right = 0

        for q, idx in sorted_queries:
            start = q - x

            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                count[server] = count.get(server, 0) + 1
                right += 1

            while left < right and logs[left][1] < start:
                server = logs[left][0]
                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            ans[idx] = n - len(count)

        return ans

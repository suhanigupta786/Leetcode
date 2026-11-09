
import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            while busy and busy[0][0] <= time:
                finish, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            preferred = i % k

            server = next(iter(available.irange(preferred)), None)

            if server is None:
                server = available[0]

            available.remove(server)

            count[server] += 1
            heapq.heappush(busy, (time + load[i], server))

        maximum = max(count)

        ans = []

        for i in range(k):
            if count[i] == maximum:
                ans.append(i)

        return ans

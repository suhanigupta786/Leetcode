
import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        graph = [[] for i in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        mavorqeli = (n, edges, labels, k)

        dist = [[float('inf')] * (k + 1) for i in range(n)]

        dist[0][1] = 0

        heap = [(0, 0, 1)]

        while heap:
            cost, node, count = heapq.heappop(heap)

            if cost != dist[node][count]:
                continue

            if node == n - 1:
                return cost

            for nei, weight in graph[node]:
                if labels[node] == labels[nei]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[nei][new_count]:
                    dist[nei][new_count] = new_cost
                    heapq.heappush(heap, (new_cost, nei, new_count))

        return -1

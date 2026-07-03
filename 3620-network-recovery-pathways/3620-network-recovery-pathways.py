from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        zalpernith = (edges, online, k)

        n = len(online)

        graph = [[] for _ in range(n)]
        indeg = [0] * n
        costs = set()

        for u, v, w in edges:
            graph[u].append((v, w))
            indeg[v] += 1
            costs.add(w)

        # Topological order
        q = deque(i for i in range(n) if indeg[i] == 0)
        topo = []

        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        vals = sorted(costs)

        def check(limit):
            INF = 10**30
            dp = [INF] * n
            dp[0] = 0

            for u in topo:
                if dp[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < limit:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    if dp[u] + w < dp[v]:
                        dp[v] = dp[u] + w

            return dp[n - 1] <= k

        lo, hi = 0, len(vals) - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if check(vals[mid]):
                ans = vals[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(u):
            visited[u] = True
            nodes = 1
            degree = len(graph[u])

            for v in graph[u]:
                if not visited[v]:
                    x, y = dfs(v)
                    nodes += x
                    degree += y

            return nodes, degree

        for i in range(n):
            if not visited[i]:
                nodes, degree = dfs(i)
                if degree // 2 == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        graph = [[] for i in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for i in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n

        timer = 0
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1

                if p != -1:
                    depth[u] = depth[p] + 1
                    parent[0][u] = p
                    prefix[u] = prefix[p] ^ (1 << (ord(s[u]) - ord('a')))
                else:
                    prefix[u] = 1 << (ord(s[u]) - ord('a'))

                for j in range(1, LOG):
                    parent[j][u] = parent[j - 1][parent[j - 1][u]]

                stack.append((u, p, 1))

                for v in graph[u]:
                    if v != p:
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = parent[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]

            return parent[0][u]

        bit = [0] * (n + 2)

        def update(i, value):
            while i <= n + 1:
                bit[i] ^= value
                i += i & -i

        def get(i):
            result = 0

            while i > 0:
                result ^= bit[i]
                i -= i & -i

            return result

        chars = list(s)
        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                if chars[u] != c:
                    old_mask = 1 << (ord(chars[u]) - ord('a'))
                    new_mask = 1 << (ord(c) - ord('a'))
                    delta = old_mask ^ new_mask

                    update(tin[u] + 1, delta)
                    update(tout[u] + 2, delta)

                    chars[u] = c
            else:
                u = int(parts[1])
                v = int(parts[2])

                ancestor = lca(u, v)

                mask_u = prefix[u] ^ get(tin[u] + 1)
                mask_v = prefix[v] ^ get(tin[v] + 1)

                path_mask = mask_u ^ mask_v
                path_mask ^= 1 << (ord(chars[ancestor]) - ord('a'))

                answer.append((path_mask & (path_mask - 1)) == 0)

        return answer

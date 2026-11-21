class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        tree = [[] for _ in range(n)]

        for i in range(1, n):
            tree[parent[i]].append(i)

        ans = [1] * n
        last = [[] for _ in range(26)]

        stack = [(0, 0)]

        while stack:
            node, state = stack.pop()
            idx = ord(s[node]) - ord('a')

            if state == 0:
                last[idx].append(node)
                stack.append((node, 1))

                for child in tree[node]:
                    stack.append((child, 0))

            else:
                if len(last[idx]) > 1:
                    new_parent = last[idx][-2]
                else:
                    new_parent = parent[node]

                if new_parent != -1:
                    ans[new_parent] += ans[node]

                last[idx].pop()

        return ans

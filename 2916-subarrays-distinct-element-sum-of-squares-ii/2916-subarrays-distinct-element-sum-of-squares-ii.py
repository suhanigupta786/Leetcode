class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        squares = [0] * (4 * n)
        lazy = [0] * (4 * n)
        last = {}
        ans = 0

        def push(node, left, right):
            if lazy[node] == 0:
                return

            val = lazy[node]
            length = right - left + 1

            squares[node] = (squares[node] + 2 * val * tree[node] + length * val * val) % MOD
            tree[node] = (tree[node] + length * val) % MOD

            if left != right:
                lazy[node * 2] += val
                lazy[node * 2 + 1] += val

            lazy[node] = 0

        def update(node, left, right, ql, qr):
            push(node, left, right)

            if right < ql or left > qr:
                return

            if ql <= left and right <= qr:
                lazy[node] += 1
                push(node, left, right)
                return

            mid = (left + right) // 2

            update(node * 2, left, mid, ql, qr)
            update(node * 2 + 1, mid + 1, right, ql, qr)

            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD
            squares[node] = (squares[node * 2] + squares[node * 2 + 1]) % MOD

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1

            update(1, 0, n - 1, left, i)

            ans = (ans + squares[1]) % MOD
            last[x] = i

        return ans
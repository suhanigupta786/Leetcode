class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        tree = [(1, [0] * k) for _ in range(4 * n)]

        def merge(a, b):
            prod1, cnt1 = a
            prod2, cnt2 = b

            prod = (prod1 * prod2) % k
            cnt = cnt1[:]

            for r in range(k):
                new_r = (prod1 * r) % k
                cnt[new_r] += cnt2[r]

            return prod, cnt

        def build(node, left, right):
            if left == right:
                x = nums[left] % k
                cnt = [0] * k
                cnt[x] = 1
                tree[node] = (x, cnt)
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, left, right, index, value):
            if left == right:
                x = value % k
                cnt = [0] * k
                cnt[x] = 1
                tree[node] = (x, cnt)
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, right, index, value)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def query(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                return tree[node]

            mid = (left + right) // 2

            if qr <= mid:
                return query(node * 2, left, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, right, ql, qr)

            a = query(node * 2, left, mid, ql, qr)
            b = query(node * 2 + 1, mid + 1, right, ql, qr)

            return merge(a, b)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            result = query(1, 0, n - 1, start, n - 1)

            ans.append(result[1][x])

        return ans
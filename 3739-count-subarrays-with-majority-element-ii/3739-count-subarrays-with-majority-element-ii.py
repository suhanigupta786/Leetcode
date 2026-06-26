from typing import List

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        while i <= n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        pref = [0]
        cur = 0

        for x in nums:
            cur += 1 if x == target else -1
            pref.append(cur)

        vals = sorted(set(pref))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        global n
        n = len(vals)

        bit = Fenwick(n)

        ans = 0

        for p in pref:
            r = rank[p]
            ans += bit.query(r - 1)
            bit.update(r, 1)

        return ans
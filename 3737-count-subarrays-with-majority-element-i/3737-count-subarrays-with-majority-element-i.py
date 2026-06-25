from typing import List

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        while i < len(self.bit):
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        pref = [0]

        s = 0
        for x in nums:
            s += 1 if x == target else -1
            pref.append(s)

        vals = sorted(set(pref))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        bit = Fenwick(len(vals))
        ans = 0

        for p in pref:
            r = rank[p]

            ans += bit.query(r - 1)   # count previous prefix sums < p

            bit.update(r, 1)

        return ans
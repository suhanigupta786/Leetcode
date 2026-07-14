from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        dp = {(0, 0): 1}

        for x in nums:
            ndp = dp.copy()

            for (g1, g2), cnt in dp.items():
                ng1 = gcd(g1, x)
                ndp[(ng1, g2)] = (ndp.get((ng1, g2), 0) + cnt) % MOD

                ng2 = gcd(g2, x)
                ndp[(g1, ng2)] = (ndp.get((g1, ng2), 0) + cnt) % MOD

            dp = ndp

        ans = 0
        for (g1, g2), cnt in dp.items():
            if g1 == g2 and g1 != 0:
                ans = (ans + cnt) % MOD

        return ans
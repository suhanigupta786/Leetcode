from typing import List
from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        ans = 0

        # Handle 1 separately
        if 1 in cnt:
            ans = cnt[1] if cnt[1] % 2 else cnt[1] - 1

        for x in list(cnt.keys()):
            if x == 1:
                continue

            cur = 0
            y = x

            while cnt[y] >= 2:
                cur += 2
                y = y * y

            if cnt[y] >= 1:
                cur += 1
            else:
                cur -= 1

            ans = max(ans, cur)

        return ans
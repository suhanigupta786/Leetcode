class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common = min(need1, need2)

        ans = common * min(costBoth, cost1 + cost2)

        if need1 > need2:
            ans += (need1 - need2) * min(cost1, costBoth)

        else:
            ans += (need2 - need1) * min(cost2, costBoth)

        return ans

class Solution:
        def climbStairs(self, n: int, costs: List[int]) -> int:
            v0 = v1 = v2 = 0
            for c in costs:
                v0, v1, v2 = v1, v2, min(v0 + 9, v1 + 4, v2 + 1) + c
            return v2
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        broken = [0] * (n - 1)

        for i in range(n - 1):
            if abs(nums[i] - nums[i + 1]) > maxDiff:
                broken[i] = 1

        pref = [0] * n
        for i in range(n - 1):
            pref[i + 1] = pref[i] + broken[i]

        ans = []

        for u, v in queries:
            if u > v:
                u, v = v, u

            ans.append(pref[v] == pref[u])

        return ans
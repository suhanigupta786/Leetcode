class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        seen = set()

        for x in nums:
            seen.add(x)
        pair = set()

        for x in nums:
            for y in nums:
                pair.add(x ^ y)
        for x in pair:
            for y in nums:
                seen.add(x ^ y)

        return len(seen)
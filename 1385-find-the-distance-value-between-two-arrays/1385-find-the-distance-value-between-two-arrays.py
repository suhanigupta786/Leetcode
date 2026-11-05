class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0

        for num in arr1:
            valid = True

            for x in arr2:
                if abs(num - x) <= d:
                    valid = False
                    break

            if valid:
                ans += 1

        return ans

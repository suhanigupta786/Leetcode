class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = []

        for x in nums:
            squares.append(x * x)

        squares.sort()

        n = len(squares)
        ans = 0

        for i in range(n):
            if i < n // 2:
                ans -= squares[i]
            else:
                ans += squares[i]

        return ans
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right= 0, sum(batteries)//n
        while left<right:
            mid= (left+right+1)//2
            total= 0
            for b in batteries:
                total+= min(mid, b)
            if total>= mid*n:
                left= mid
            else:
                right= mid-1 
        return left




        # batteries.sort()
        # left, right = 0, sum(batteries) // n
        # while left < right:
        #     mid = (left + right + 1) // 2
        #     total = 0
        #     for b in batteries:
        #         total += min(b, mid)
        #     if total >= mid * n:
        #         left = mid
        #     else:
        #         right = mid - 1
        # return left
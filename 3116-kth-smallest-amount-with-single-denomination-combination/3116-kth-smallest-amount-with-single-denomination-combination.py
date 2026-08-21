from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            # Inclusion-exclusion
            for mask in range(1, 1 << n):
                common = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        common = lcm(common, coins[i])

                        if common > x:
                            break

                else:
                    amount = x // common

                    if bits % 2 == 1:
                        total += amount
                    else:
                        total -= amount

            return total

        # kth amount cannot be larger than k * smallest coin
        left = 1
        right = k * min(coins)

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
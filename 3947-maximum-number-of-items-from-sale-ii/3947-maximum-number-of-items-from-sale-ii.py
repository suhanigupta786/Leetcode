class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        max_factor = 0
        min_price = float('inf')

        for factor, price in items:
            max_factor = max(max_factor, factor)
            min_price = min(min_price, price)

        freq = [0] * (max_factor + 1)

        for factor, price in items:
            freq[factor] += 1

        gain = [0] * (max_factor + 1)

        for factor in range(1, max_factor + 1):
            total = 0

            for multiple in range(factor, max_factor + 1, factor):
                total += freq[multiple]

            gain[factor] = total - 1

        boosted = []

        for factor, price in items:
            if gain[factor] > 0 and price <= 2 * min_price:
                boosted.append((price, gain[factor]))

        boosted.sort()

        ans = 0

        for price, count in boosted:
            if budget < price:
                break

            buy = min(count, budget // price)

            ans += buy * 2
            budget -= buy * price

        ans += budget // min_price

        return ans

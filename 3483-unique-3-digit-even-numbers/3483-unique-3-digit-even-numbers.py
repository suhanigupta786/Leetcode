class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_nums = set()
        n = len(digits)
        for i in range(n):   # ones place (must be even)
            if digits[i] % 2 != 0:
                continue
            for j in range(n):   # tens place
                if j == i:
                    continue
                for k in range(n):   # hundreds place
                    if k == i or k == j:
                        continue
                    if digits[k] == 0:   # leading zero not allowed
                        continue
                    num = digits[k] * 100 + digits[j] * 10 + digits[i]
                    unique_nums.add(num)
        return len(unique_nums)

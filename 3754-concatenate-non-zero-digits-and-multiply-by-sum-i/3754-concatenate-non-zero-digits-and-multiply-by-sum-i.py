class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = ""
        digit_sum = 0

        for ch in str(n):
            if ch != '0':
                s += ch
                digit_sum += int(ch)

        if not s:
            return 0

        return int(s) * digit_sum
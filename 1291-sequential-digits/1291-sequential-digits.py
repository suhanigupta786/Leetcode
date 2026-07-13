class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        s = "123456789"

        for length in range(2, 10):
            for start in range(10 - length):
                num = int(s[start:start + length])
                if low <= num <= high:
                    ans.append(num)

        return ans
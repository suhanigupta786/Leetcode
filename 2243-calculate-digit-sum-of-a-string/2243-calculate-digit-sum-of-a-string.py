class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new = ""

            for i in range(0, len(s), k):
                total = 0

                for j in range(i, min(i + k, len(s))):
                    total += int(s[j])

                new += str(total)

            s = new

        return s

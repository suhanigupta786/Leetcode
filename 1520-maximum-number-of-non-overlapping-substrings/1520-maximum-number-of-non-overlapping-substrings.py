class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        for i in range(n):
            x = ord(s[i]) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        for c in range(26):
            if first[c] == n:
                continue

            left = first[c]
            right = last[c]
            i = left
            valid = True

            while i <= right:
                x = ord(s[i]) - ord('a')

                if first[x] < left:
                    valid = False
                    break

                right = max(right, last[x])
                i += 1

            if valid:
                intervals.append((right, left))

        intervals.sort()

        ans = []
        prev = -1

        for right, left in intervals:
            if left > prev:
                ans.append(s[left:right + 1])
                prev = right

        return ans
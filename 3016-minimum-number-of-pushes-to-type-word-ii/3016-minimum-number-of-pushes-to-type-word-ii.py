from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)

        counts = sorted(freq.values(), reverse=True)

        ans = 0

        for i, count in enumerate(counts):
            pushes = i // 8 + 1
            ans += count * pushes

        return ans
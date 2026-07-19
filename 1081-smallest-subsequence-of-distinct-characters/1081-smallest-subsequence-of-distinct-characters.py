class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        stack = []
        seen = set()

        for ch in s:
            freq[ch] -= 1

            if ch in seen:
                continue

            while (
                stack
                and ch < stack[-1]
                and freq[stack[-1]] > 0
            ):
                removed = stack.pop()
                seen.remove(removed)

            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)
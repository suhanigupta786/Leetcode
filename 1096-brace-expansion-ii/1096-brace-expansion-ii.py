class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def merge(a, b):
            result = set()

            for x in a:
                for y in b:
                    result.add(x + y)

            return result

        def solve(s):
            parts = []
            current = set()

            i = 0

            while i < len(s):

                if s[i] == ',':
                    parts.append(current)
                    current = set()
                    i += 1

                elif s[i] == '{':
                    count = 1
                    j = i + 1

                    while count:
                        if s[j] == '{':
                            count += 1
                        elif s[j] == '}':
                            count -= 1
                        j += 1

                    inside = solve(s[i + 1:j - 1])

                    if not current:
                        current = inside
                    else:
                        current = merge(current, inside)

                    i = j

                else:
                    word = ""

                    while i < len(s) and s[i].isalpha():
                        word += s[i]
                        i += 1

                    if not current:
                        current.add(word)
                    else:
                        current = merge(current, {word})

            parts.append(current)

            result = set()

            for part in parts:
                result.update(part)

            return result

        return sorted(solve(expression))
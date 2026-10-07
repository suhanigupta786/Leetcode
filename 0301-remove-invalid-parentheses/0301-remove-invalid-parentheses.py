class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)
        ans = set()

        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        def dfs(i, left_remove, right_remove, left_count, right_count, path):
            if i == n:
                if left_remove == 0 and right_remove == 0:
                    ans.add(path)
                return

            if n - i < left_remove + right_remove:
                return

            if left_count < right_count:
                return

            ch = s[i]

            if ch == '(':
                if left_remove > 0:
                    dfs(i + 1, left_remove - 1, right_remove,
                        left_count, right_count, path)

                dfs(i + 1, left_remove, right_remove,
                    left_count + 1, right_count, path + '(')

            elif ch == ')':
                if right_remove > 0:
                    dfs(i + 1, left_remove, right_remove - 1,
                        left_count, right_count, path)

                if left_count > right_count:
                    dfs(i + 1, left_remove, right_remove,
                        left_count, right_count + 1, path + ')')

            else:
                dfs(i + 1, left_remove, right_remove,
                    left_count, right_count, path + ch)

        dfs(0, left_remove, right_remove, 0, 0, "")

        return list(ans)
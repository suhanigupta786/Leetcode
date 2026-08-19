class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for r, seat in reservedSeats:
            rows[r] = rows.get(r, 0) | (1 << seat)

        ans = (n - len(rows)) * 2

        for mask in rows.values():
            left = True
            middle = True
            right = True

            # Seats 2,3,4,5
            for seat in range(2, 6):
                if mask & (1 << seat):
                    left = False
                    break

            # Seats 4,5,6,7
            for seat in range(4, 8):
                if mask & (1 << seat):
                    middle = False
                    break

            # Seats 6,7,8,9
            for seat in range(6, 10):
                if mask & (1 << seat):
                    right = False
                    break

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans
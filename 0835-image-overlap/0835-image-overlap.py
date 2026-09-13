class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        ones1 = []
        ones2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones1.append((i, j))

                if img2[i][j] == 1:
                    ones2.append((i, j))

        count = {}
        ans = 0

        for x1, y1 in ones1:
            for x2, y2 in ones2:
                dx = x1 - x2
                dy = y1 - y2

                if (dx, dy) not in count:
                    count[(dx, dy)] = 0

                count[(dx, dy)] += 1
                ans = max(ans, count[(dx, dy)])

        return ans
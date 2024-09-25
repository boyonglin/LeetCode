from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        arrows = 1
        shot = points[0][1]

        # always shooting the arrow at the earliest possible point, which happens to be the end of the current balloon
        for start, end in points[1:]:
            if start > shot:
                arrows += 1
                shot = end

        return arrows

# Testcase
points = [[10,16],[2,8],[1,6],[7,12]]

sol = Solution()
print(sol.findMinArrowShots(points))
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = [0] * n

        left_wall = height[0]
        for i in range(1, n):
            if height[i] < left_wall:
                water[i] = left_wall - height[i]
            else:
                left_wall = height[i]

        right_wall = 0
        for i in range(n - 1, 0, -1):
            if height[i] < right_wall:
                water[i] = min(water[i], right_wall - height[i])
            else:
                right_wall = height[i]
                water[i] = 0

        return sum(water)

# Testcase
height = [0,1,0,2,1,0,1,3,2,1,2,1]

sol = Solution()
print(sol.trap(height))
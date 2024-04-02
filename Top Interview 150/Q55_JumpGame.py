from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reachable = 0

        for i in range(n):
            # if current index is not reachable
            if i > max_reachable:
                return False

            max_reachable = max(max_reachable, i + nums[i])

            # if can reach the last index
            if max_reachable >= n - 1:
                return True

# Testcase
nums = [2,3,1,1,4]

sol = Solution()
print(sol.canJump(nums))
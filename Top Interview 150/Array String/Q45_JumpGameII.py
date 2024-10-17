from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_reachable = 0
        stop = 0
        jump = 0

        for i in range(n):
            # special case check
            if i > max_reachable or n == 1:
                return 0

            # energy assurance
            max_reachable = max(max_reachable, i + nums[i])

            # early stop check
            if max_reachable >= n - 1:
                return jump + 1

            # add energy
            if i == stop:
                jump += 1
                stop = max_reachable

        return jump

# Testcase
nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]

sol = Solution()
print(sol.jump(nums))
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k %= len(nums)
        k = len(nums) - k
        nums[:] = nums[k:] + nums[:k]


# Testcase
nums = [1,2,3,4,5,6,7]
k = 3

sol = Solution()
sol.rotate(nums, k)
print(nums)

nums = [1,2]
k = 5

sol.rotate(nums, k)
print(nums)
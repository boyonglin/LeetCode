from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        forward = [1] * n
        reverse = [1] * n

        for i in range(1, n):
            forward[i] = forward[i-1] * nums[i-1]

        for i in range(1, n):
            reverse[i] = reverse[i-1] * nums[n-i]

        for i in range(n):
            nums[i] = forward[i] * reverse[n-i-1]

        return nums

# Testcase
nums = [1,2,3,4]

sol = Solution()
print(sol.productExceptSelf(nums))
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_len = len(nums) + 1

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return 0 if min_len == len(nums) + 1 else min_len

# Testcase
target = 11
nums = [1,1,1,1,1,1,1,1]

sol = Solution()
print(sol.minSubArrayLen(target, nums))
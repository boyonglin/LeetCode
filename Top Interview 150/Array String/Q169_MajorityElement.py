from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # method 1
        n = len(nums)
        element_dict = dict()

        for num in nums:
            if num in element_dict:
                element_dict[num] += 1
            else:
                element_dict[num] = 1

        for key, value in element_dict.items():
            if value > n/2:
                return key
            
        # method 2
        # n = len(nums) // 2
        # nums.sort()
        # return nums[n]

# Testcase
nums = [2,2,1,1,1,2,2]

sol = Solution()
print(sol.majorityElement(nums))

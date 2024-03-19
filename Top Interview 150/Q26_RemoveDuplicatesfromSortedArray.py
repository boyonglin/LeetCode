from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # method 1
        nums_set = set(nums)
        nums.clear()
        nums.extend(sorted(nums_set))

        return len(nums)

        # method 2
        # seen = set()
        # index = 0

        # for i in range(len(nums)):
        #     if nums[i] not in seen:
        #         nums[index] = nums[i]
        #         seen.add(nums[i])
        #         index += 1

        # del nums[index:]
        # return index

# Testcase
nums = [-1,0,0,0,0,3,3]

sol = Solution()
print(sol.removeDuplicates(nums), nums)
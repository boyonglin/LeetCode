from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        index = 0

        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[index] = nums[i]
                seen.add(nums[i])
                index += 1

        del nums[index:]
        return index

# Testcase
nums = [0,0,1,1,1,2,2,3,3,4]

sol = Solution()
print(sol.removeDuplicates(nums), nums)
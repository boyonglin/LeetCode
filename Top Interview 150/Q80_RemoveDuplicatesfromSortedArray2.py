from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = list()
        index = 0

        for i in range(len(nums)):
            if seen.count(nums[i]) < 2:
                nums[index] = nums[i]
                seen.append(nums[i])
                index += 1

        del nums[index:]
        return index

# Testcase
nums = [0,0,1,1,1,1,2,3,3]

sol = Solution()
print(sol.removeDuplicates(nums), nums)
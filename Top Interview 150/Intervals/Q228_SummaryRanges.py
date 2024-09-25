from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        temp = []

        for i in range(len(nums)):
            temp.append(nums[i])

            if nums[i] + 1 not in nums:
                if len(temp) == 1:
                    res.append(str(temp[0]))
                else:
                    res.append(str(temp[0]) + "->" + str(temp[-1]))

                temp = []

        return res


# Testcase
nums = [0,1,2,4,5,7]

sol = Solution()
print(sol.summaryRanges(nums))
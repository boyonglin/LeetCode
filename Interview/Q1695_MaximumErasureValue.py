from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        uni_map = {}
        start = 0
        res = 0
        cur = 0

        for i in range(len(nums)):
            if nums[i] in uni_map and start <= uni_map[nums[i]]:

                for j in range(start, uni_map[nums[i]] + 1):
                    cur -= nums[j]

                start = uni_map[nums[i]] + 1

            cur += nums[i]
            uni_map[nums[i]] = i
            res = max(res, cur)

        return res

# Testcases
nums = [5,2,1,2,5,2,1,2,5]

sol = Solution()
print(sol.maximumUniqueSubarray(nums))
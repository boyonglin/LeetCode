from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ts_set = set() # two-sum set
        ts_map = dict() # two-sum hash map

        for i in range(n):
            ts_map[nums[i]] = i # duplicate key (num) will be overwritten

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                f = nums[i]  # first
                s = nums[j]  # second
                t = -(f + s) # third

                if t in ts_map and ts_map[t] > j:
                    ts_set.add((f, s, t))

        return list(ts_set)

# Testcase
nums = [-1,0,1,2,-1,-4]

sol = Solution()
print(sol.threeSum(nums))
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue

            lack = target - numbers[i]
            left, right = i+1, len(numbers)-1

            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == lack:
                    return [i + 1, mid + 1]
                elif numbers[mid] < lack:
                    left = mid + 1
                else:
                    right = mid - 1

# Testcase
numbers = [2,7,11,15]
target = 9

sol = Solution()
print(sol.twoSum(numbers, target))
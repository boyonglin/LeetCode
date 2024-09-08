from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left
        for i in range(n - 1, 0, -1):
            if ratings[i] < ratings[i - 1]:
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)

        return sum(candies)

# Testcase
ratings = [1,3,4,5,2]

sol = Solution()
print(sol.candy(ratings))
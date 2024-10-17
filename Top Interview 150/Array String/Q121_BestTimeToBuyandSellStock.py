from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy

        return profit

# Testcase
prices = [7,1,5,3,6,4]

sol = Solution()
print(sol.maxProfit(prices))
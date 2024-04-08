from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        n = len(gas)
        start = 0
        tank = 0

        for i in range(n):
            tank += gas[i] - cost[i]

            # If tank < 0, means cannot reach next station
            if tank < 0:
                start = i + 1
                tank = 0

        return start

# Testcase
gas = [5,5,1,3,4]
cost = [8,1,7,1,1]

sol = Solution()
print(sol.canCompleteCircuit(gas, cost))
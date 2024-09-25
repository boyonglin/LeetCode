from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        start = intervals[0][0]
        end = intervals[0][1]
        res = []

        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        res.append([start, end])

        return res

# Testcase
intervals = [[1,3]]
newInterval = [2,5]

sol = Solution()
print(sol.insert(intervals, newInterval))
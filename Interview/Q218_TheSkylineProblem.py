import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        bamboo = []

        for building in buildings:
            bamboo.append((building[0], -building[2]))
            bamboo.append((building[1], building[2]))
        bamboo.sort(key=lambda x: (x[0], x[1]))

        # line sweep
        height_heap = [0]
        skyline = []
        height_count = {0: 1}

        for x, h in bamboo:
            if h < 0:  # building start
                heapq.heappush(height_heap, h)  # store negative value turn min-heap (heapq) to max-heap
                height_count[-h] = height_count.get(-h, 0) + 1
            else:  # building end
                height_count[h] -= 1
                if height_count[h] == 0:
                    del height_count[h]

            # lazy deletion
            while height_heap and -height_heap[0] not in height_count:
                heapq.heappop(height_heap)

            # get max
            max_height = -height_heap[0]

            # height changed
            if not skyline or skyline[-1][1] != max_height:
                skyline.append([x, max_height])

        return skyline

buildings = [[1,2,1],[1,2,2],[1,2,3],[2,3,1],[2,3,2],[2,3,3]]
sol = Solution()
print(sol.getSkyline(buildings))
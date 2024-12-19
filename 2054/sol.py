from typing import List
import heapq

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        minh = []
        maxv, maxs = 0, 0

        start_sort = sorted(events, key=lambda x: x[0])

        for e in start_sort:
            
            while minh and minh[0][0] < e[0]:
                maxv = max(maxv, minh[0][1])
                heapq.heappop(minh)
            
            maxs = max(maxs, maxv + e[2])
            heapq.heappush(minh, [e[1], e[2]])

        return maxs

if __name__ == "__main__":
    events = [[1,3,2],[4,5,2],[2,4,3]]
    events2 = [[1,3,2],[4,5,2],[1,5,5]]
    events3 = [[1,5,3],[1,5,1],[6,6,5]]
    s = Solution()
    print(s.maxTwoEvents(events))
    print(s.maxTwoEvents(events2))
    print(s.maxTwoEvents(events3))
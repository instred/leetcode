from typing import List
from math import  sqrt, floor
from heapq import heapify, heappop, heappush

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapify(gifts)
        while k > 0:
            maxx = heappop(gifts)
            heappush(gifts, -floor(sqrt(-maxx)))
            k-=1
        return -sum(gifts)



if __name__ == "__main__":
    s = Solution()
    gifts = [25,64,9,4,100]
    k = 4
    gifts2 = [1,1,1,1]
    k2 = 4
    print(s.pickGifts(gifts, k))
    print(s.pickGifts(gifts2, k2))
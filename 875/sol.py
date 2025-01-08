from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_pile = max(piles)
        min_speed = max_pile
        i, j = 1, max_pile
        while i <= j:
            
            mid = (i+j)//2
            piles_hours = 0
            for p in piles:
                piles_hours += -(-p//mid)

            if piles_hours <= h:
                j = mid-1
                min_speed = min(min_speed, mid)
                
            else:
                i = mid+1
        return min_speed




if __name__ == "__main__":
    sol = Solution()
    piles = [3,6,7,11]  
    h = 8  
    piles2 = [30,11,23,4,20]  
    h2 = 5  
    piles3 = [30,11,23,4,20]  
    h3 = 6
    print(sol.minEatingSpeed(piles, h))
    print(sol.minEatingSpeed(piles2, h2))
    print(sol.minEatingSpeed(piles3, h3))

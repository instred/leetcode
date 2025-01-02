from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        n = len(height)
        l, r = 0, n-1
        maxl, maxr = 0, 0
        while l < r:
            if height[l] <= height[r]:
                if maxl - height[l] > 0:
                    area += maxl - height[l]
                maxl = max(maxl, height[l])
                l += 1
            else:
                if maxr - height[r] > 0:
                    area += maxr - height[r]
                maxr = max(maxr, height[r])
                r -= 1

        return area


if __name__ == "__main__":
    sol = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(sol.trap(height))
    height2 = [4,2,3]
    
    print(sol.trap(height2))
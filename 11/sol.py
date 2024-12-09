from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ans = 0
        while l <= r:
            if height[l] < height[r]:
                area = (r-l)*height[l]
                ans = max(area, ans)
                l += 1
            
            else:
                area = (r-l)*height[r]
                ans = max(area, ans)
                r -= 1

        return ans

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    height2 = [1,1]
    height3 = [8,7,2,1]
    s = Solution()
    print(s.maxArea(height))
    print(s.maxArea(height2))
    print(s.maxArea(height3))
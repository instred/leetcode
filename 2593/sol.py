from typing import List
import heapq

class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        n = len(nums)
        marked = set()
        sorted_nums = []

        for i in range(n):
            sorted_nums.append((nums[i], i))
        sorted_nums.sort(key=lambda x: x[0])
        
        for num, idx in sorted_nums:
            
            if idx not in marked:
                score += num
                marked.add(idx)
                if idx > 0: marked.add(idx-1)
                if idx < n-1: marked.add(idx+1)

        return score



if __name__ == "__main__":
    nums = [2,1,3,4,5,2]
    nums2 = [2,3,5,1,3,2]
    s = Solution()
    print(s.findScore(nums))
    print(s.findScore(nums2))
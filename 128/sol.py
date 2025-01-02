from typing import List
import heapq

class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        nums = list(num_set)
        heapq.heapify(nums)
        streak = 0
        while nums:
            curr = heapq.heappop(nums)
            curr_streak = 1
            while curr+1 in num_set:
                curr = heapq.heappop(nums)
                curr_streak += 1
            streak = max(streak, curr_streak)
        return streak

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        streak = 0

        for num in num_set:
            if num-1 not in num_set:
                curr = 1
                while (num+curr) in num_set:
                    curr += 1
                streak = max(streak, curr)

        return streak

        

if __name__ == "__main__":
    sol = Solution()
    nums = [100,4,200,1,3,2]
    nums2 = [0,3,7,2,5,8,4,6,0,1]
    print(sol.longestConsecutive(nums))
    print(sol.longestConsecutive(nums2))

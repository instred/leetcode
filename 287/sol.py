from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
            
        return slow

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,4,2,2]  
    nums2 = [3,1,3,4,2]  
    nums3 = [3,3,3,3,3]
    print(sol.findDuplicate(nums))
    print(sol.findDuplicate(nums2))
    print(sol.findDuplicate(nums3))
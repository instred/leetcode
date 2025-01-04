from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid-1
            else:
                i = mid+1
        return -1     
        

if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,3,5,9,12]  
    target = 9  
    nums2 = [-1,0,3,5,9,12]  
    target2 = 2
    print(sol.search(nums, target))
    print(sol.search(nums2, target2))
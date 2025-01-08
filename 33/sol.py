from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:

            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            # left sorted
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

                    


if __name__ == "__main__":
    sol = Solution()
    nums = [4,5,6,7,0,1,2]  
    target = 0  
    nums2 = [4,5,6,7,0,1,2]  
    target2 = 3  
    nums3 = [1]  
    target3 = 0
    print(sol.search(nums, target))
    print(sol.search(nums2, target2))
    print(sol.search(nums3, target3))
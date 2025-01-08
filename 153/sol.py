from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        ans = 5000
        while l <= r:
            
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break

            mid = (l+r) //2
            ans = min(ans, nums[mid])
            
            if nums[l] <= nums[mid]:
                l = mid + 1

            else:
                r = mid -1

        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [3,4,5,1,2]  
    nums2 = [4,5,6,7,0,1,2]  
    nums3 = [11,13,15,17]
    print(sol.findMin(nums))
    print(sol.findMin(nums2))
    print(sol.findMin(nums3))
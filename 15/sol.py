from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j, k = i+1, len(nums)-1
            while j < k:
                c_sum = nums[j] + nums[k]
                if c_sum > -nums[i]:
                    k -= 1
                elif c_sum < -nums[i]:
                    j += 1
                else:
                    t = [nums[i], nums[j], nums[k]]
                    triplets.append(t)
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return triplets    


if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    nums2 = [0,1,1]
    nums3 = [-2,0,1,1,2]
    print(sol.threeSum(nums))
    print(sol.threeSum(nums2))
    print(sol.threeSum(nums3))
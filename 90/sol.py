from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()
        subset = []

        def backtrack(i):
            if i == len(nums):
                ans.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()


            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)

        backtrack(0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,2]  
    nums2 = [0]
    print(sol.subsetsWithDup(nums))
    print(sol.subsetsWithDup(nums2))
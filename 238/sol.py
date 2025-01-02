from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, n-1
        ans = [1]*n
        pref = 1
        suff = 1
        while i < n:
            ans[i] = pref
            pref *= nums[i]
            i += 1
        while j > -1:
            ans[j] *= suff
            suff *= nums[j]
            j -= 1
        return ans
        


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    nums2 = [-1,1,0,-3,3]
    nums3 = [4,3,2,1,2]
    print(sol.productExceptSelf(nums))
    print(sol.productExceptSelf(nums2))
    print(sol.productExceptSelf(nums3))
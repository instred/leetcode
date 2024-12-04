from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        looked = {}
        for i in range(len(nums)):
            if target - nums[i] in looked:
                return [looked[target-nums[i]], i]
            looked[nums[i]] = i

if __name__ == "__main__":
    s = Solution()  
    nums = [2,7,11,15]
    target = 9
    nums2 = [3,2,4]
    target2 = 6
    nums3 = [3,3]
    target3 = 6
    print(s.twoSum(nums3, target3))


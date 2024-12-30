from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniq = set()

        for n in nums:
            if n in uniq:
                return True
            uniq.add(n)
        return False


if __name__ == "__main__":
    nums = [3,1]
    nums2 = [1,2,3,4]
    nums3 = [1,1,1,3,3,4,3,2,4,2]
    s = Solution()
    print(s.containsDuplicate(nums))
    print(s.containsDuplicate(nums2))
    print(s.containsDuplicate(nums3))


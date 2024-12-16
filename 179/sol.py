from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]

        def cmp(x, y):
            if x+y > y+x:
                return -1
            elif x+y < y+x:
                return 1
            else:
                return 0

        nums.sort(key=cmp_to_key(cmp))
        ans = ''.join(nums)
        return ans if set(ans) != 0 else 0

if __name__ == "__main__":
    nums = [10,2]
    nums2 = [3,30,34,5,9]
    s = Solution()
    print(s.largestNumber(nums))
    print(s.largestNumber(nums2))
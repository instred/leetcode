from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        chrs = {}

        for n in nums:
            chrs[n] = chrs.get(n, 1) +1

        pairs = sorted(chrs.items(), key=lambda x: x[1], reverse=True)
        ans = [i[0] for i in pairs[:k]]
        return ans

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    nums2 = [1]
    k2 = 1
    s = Solution()
    print(s.topKFrequent(nums, k))
    print(s.topKFrequent(nums2, k2))
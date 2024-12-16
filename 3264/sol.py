from typing import List
import heapq


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        ans = nums[:]
        while k > 0:
            i = ans.index(min(ans))
            ans[i] *= multiplier

            k -= 1
        return ans
    
    
class Solution2:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pairs = []
        ans = []
        for i in range(len(nums)):
            heapq.heappush(pairs, (nums[i], i))

        while k > 0:
            minn = heapq.heappop(pairs)
            multiplied = (minn[0]*multiplier, minn[1])
            heapq.heappush(pairs, multiplied)
            
            k-=1

        return [x[0] for x in sorted(pairs, key=lambda x: x[1])]



if __name__ == "__main__":
    nums = [2,1,3,5,6]
    k = 5
    multiplier = 2
    nums2 = [1,2]
    k2 = 3
    multiplier2 = 4
    s = Solution2()
    print(s.getFinalState(nums,k,multiplier))
    print(s.getFinalState(nums2,k2,multiplier2))
    # print(s.getFinalState(nums3,k3,multiplier3))
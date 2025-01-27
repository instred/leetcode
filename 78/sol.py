from typing import List

class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                ans.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return ans
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            print(res, num)
            res += [subset + [num] for subset in res]
        
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]  
    nums2 = [0]
    print(sol.subsets(nums))
    print(sol.subsets(nums2))
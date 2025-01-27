from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        perm = []
        visited = [False] * len(nums)

        def backtrack():

            if len(perm) == len(nums):
                ans.append(perm.copy())
                return
            
            for j in range(len(nums)):
                if not visited[j]:
                    perm.append(nums[j])
                    visited[j] = True
                    backtrack()
                    perm.pop()
                    visited[j] = False
                

        backtrack()
        return ans
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]  
    nums2 = [0,1]  
    nums3 = [1]
    print(sol.permute(nums))
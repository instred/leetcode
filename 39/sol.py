from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        subset = []

        def dfs(i, total):
            
            if total == target:
                ans.append(subset.copy()) 
                return
            if i >= len(candidates) or total > target:
                return
            subset.append(candidates[i])
            dfs(i, total + candidates[i])
            subset.pop()
            dfs(i+1, total)

        dfs(0, 0)
        return ans

if __name__ == "__main__":
    sol = Solution()
    candidates = [2,3,6,7]  
    target = 7  
    candidates2 = [2,3,5]  
    target2 = 8  
    candidates3 = [2]  
    target3 = 1
    print(sol.combinationSum(candidates, target))
    print(sol.combinationSum(candidates2, target2))
    print(sol.combinationSum(candidates3, target3))
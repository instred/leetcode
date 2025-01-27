from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        ans = []
        subset = []
        # print(candidates)
        def dfs(i, total):
            
            if total == target:
                ans.append((subset.copy())) 
                return
                
            if i >= len(candidates) or total > target:
                return
            
            subset.append(candidates[i])
            dfs(i+1, total + candidates[i])
            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total)

        dfs(0, 0)
        return ans

if __name__ == "__main__":
    sol = Solution()
    candidates = [10,1,2,7,6,1,5]  
    target = 8  
    candidates2 = [2,5,2,1,2]  
    target2 = 5
    print(sol.combinationSum2(candidates, target))
    print(sol.combinationSum2(candidates2, target2))

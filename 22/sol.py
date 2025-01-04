from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        curr = []
        def backtrack(opened, closed):
            if opened == closed == n:
                ans.append("".join(curr))
                return 
            if opened > closed:
                curr.append(')') 
                backtrack(opened, closed+1)
                curr.pop()
            
            if opened < n:
                curr.append('(') 
                backtrack(opened+1, closed)
                curr.pop()
        backtrack(0,0)
        return ans

if __name__ == "__main__":

    sol = Solution()
    n = 3
    n2 = 1
    print(sol.generateParenthesis(n))
    print(sol.generateParenthesis(n2))
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        ans = []
        if not digits:
            return ans
        num_to_let = {
            "2" : 'abc',
            "3" : 'def',
            "4" : 'ghi',
            "5" : 'jkl',
            "6" : 'mno',
            "7" : 'pqrs',
            "8" : 'tuv',
            "9" : 'wxyz'
        }

        def backtrack(i, part):
            if len(part) == len(digits):
                ans.append(part)
                return

            for ch in num_to_let[digits[i]]:    
                backtrack(i+1, part + ch)
            
        backtrack(0, "")
        return ans

            
            


if __name__ == "__main__":
    sol = Solution()
    digits = "23"  
    digits2 = ""  
    digits3 = "2"
    print(sol.letterCombinations(digits))
    print(sol.letterCombinations(digits2))
    print(sol.letterCombinations(digits3))
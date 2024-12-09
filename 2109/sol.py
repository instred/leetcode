from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.reverse()
        ans = ''
        curr = None
        for i in range(len(s)):
            if not curr and spaces:
                curr = spaces.pop()
            if i == curr:
                curr = None
                ans += " "
            ans += s[i]

        return ans
    
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = list(s)
        for sp in spaces:
            ans[sp] = " " + ans[sp]

        return ''.join(ans)

if __name__ == "__main__":
    sol = Solution()
    s = "LeetcodeHelpsMeLearn"
    spaces = [8,13,15]
    s2 = "icodeinpython"
    spaces2 = [1,5,7,9]
    s3 = "spacing"
    spaces3 = [0,1,2,3,4,5,6]
    print(sol.addSpaces(s,spaces))
    print(sol.addSpaces(s2,spaces2))
    print(sol.addSpaces(s3,spaces3))

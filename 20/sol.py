class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        top = ''
        pairs = {'(' : ')', '[' : ']', '{' : '}'}
        for ch in s:
            if not stack:
                stack.append(ch)
                continue
            top = stack[-1]
            if top not in pairs or pairs[top] != ch:
                stack.append(ch)
            else:
                stack.pop()

        return True if not stack else False
            



if __name__ == "__main__":
    sol = Solution()
    s = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([])"
    print(sol.isValid(s))
    print(sol.isValid(s2))
    print(sol.isValid(s3))
    print(sol.isValid(s4))
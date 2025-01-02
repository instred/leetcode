import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        expr = r'[^a-zA-Z0-9]'
        s = re.sub(expr, '', s)
        s= s.lower()
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    s3 = " "
    print(sol.isPalindrome(s))
    print(sol.isPalindrome(s2))
    print(sol.isPalindrome(s3))
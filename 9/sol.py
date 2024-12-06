class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i,j = 0, len(x)-1
        while i < j:
            if x[i] == x[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
        



if __name__ == "__main__":
    x = 1221
    x2 = -121
    s = Solution()
    print(s.isPalindrome(x))
    print(s.isPalindrome(x2))
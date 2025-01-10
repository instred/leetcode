class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        charset = set(s)

        for ch in charset:
            i, j, count = 0,0,0

            while j < len(s):
                if s[j] == ch:
                    count += 1
                
                while (j - i + 1) - count > k:
                    if s[i] == ch:
                        count -= 1
                    i += 1

                ans = max(ans, j - i + 1)
                j += 1
                
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "ABAB"  
    k = 2  
    s2 = "AABABBA"  
    k2 = 1
    print(sol.characterReplacement(s, k))
    print(sol.characterReplacement(s2, k2))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        ans = 0
        i, j = 0, 0
        while j < len(s):

            while s[j] in curr:
                curr.remove(s[i])
                i += 1

            curr.add(s[j])
            j+=1
            ans = max(ans, len(curr))

        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"  
    s2 = "dvdf"  
    s3 = "pwwkew"
    s4 = "busvutpwmu"
    print(sol.lengthOfLongestSubstring(s))
    print(sol.lengthOfLongestSubstring(s2))
    print(sol.lengthOfLongestSubstring(s3))
    print(sol.lengthOfLongestSubstring(s4))
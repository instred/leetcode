
class Solution:
    def maxScore(self, s: str) -> int:
        l_sum = 1 if s[0] == '0' else 0
        r_sum = s[1:].count('1')
        max_sum = l_sum+r_sum
        i = 1
        while i < len(s)-1:
            if s[i] == '0':
                l_sum += 1
            else:
                r_sum -= 1
            max_sum = max(max_sum, l_sum+r_sum)
            i += 1
        return max_sum
    

if __name__ == "__main__":
    s = "011101"
    s2 = "00111"
    s3 = "1111"

    sol = Solution()
    print(sol.maxScore(s))
    print(sol.maxScore(s2))
    print(sol.maxScore(s3))
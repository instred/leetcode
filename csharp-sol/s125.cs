using System.Text.RegularExpressions;

namespace csharp_sol 
{
    public static class S125 
    {
        public static bool IsPalindrome(string s) 
        {

            char[] cleared = [.. s.ToLower().Where(char.IsLetterOrDigit)];
            s = new string(cleared);
            int l = 0;
            int r = s.Length - 1;

            while (l < r)
            {
                if (s[l] != s[r])
                {
                    return false;
                }
                l++;
                r--;
            }
            return true;

        }
    }
}
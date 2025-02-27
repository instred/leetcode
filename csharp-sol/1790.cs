namespace csharp_sol 
{
    public static class S1790 
    {
        public static bool AreAlmostEqual(string s1, string s2) 
        {
            int diffCount = 0;
            int diff1 = -1;
            int diff2 = -1;
            for (int i = 0; i < s1.Length; i++)
            {
                if (s1[i] != s2[i])
                {
                    diffCount++;
                    if (diffCount == 1) diff1 = i;
                    else if (diffCount == 2) diff2 = i;
                    if (diffCount > 2) return false;
                }
            }
            if (diffCount == 0) return true;
            else if (diffCount == 2)
            {
                return s1[diff1] == s2[diff2] && s1[diff2] == s2[diff1];
            }
            else return false;
        }
    }
}

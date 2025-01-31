namespace csharp_sol 
{
    public static class S242 
    {
        public static bool IsAnagram(string s, string t) 
        {
            if (s.Length != t.Length)
            {
                return false;
            }
            Dictionary<char, int> map_s = new();
            for (int i = 0; i < s.Length; i++)
            {
                if (map_s.ContainsKey(s[i]))
                {
                    map_s[s[i]]++;
                }
                else
                {
                    map_s[s[i]] = 1;
                }
            }
            for (int i = 0; i < t.Length; i++)
            {
                if (map_s.ContainsKey(t[i]))
                {
                    map_s[t[i]]--;
                }

            }
            foreach (var item in map_s)
            {
                if (item.Value != 0)
                {
                    return false;
                }
            }

            return true;

        }
    }
}
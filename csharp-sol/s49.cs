namespace csharp_sol 
{
    public static class S49 
    {
        public static IList<IList<string>> GroupAnagrams(string[] strs) 
        {
            Dictionary<string, List<string>> groups = [];
            foreach (string item in strs)
            {
                // char[] chars = item.ToArray();
                char[] chars = [.. item];
                Array.Sort(chars);
                string s = new(chars);
                // Console.WriteLine(s);

                if (groups.ContainsKey(s))
                {
                    groups[s].Add(item);
                }
                else
                {
                    groups[s] = [item];
                }
            }    

            List<IList<string>> ans = [];

            foreach (var item in groups)
            {
                ans.Add(item.Value);
            }
            return ans;
            
            // return [.. groups.Values.Cast<IList<string>>()];
        }
    }
}
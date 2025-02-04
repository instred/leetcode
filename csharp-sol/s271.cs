using System.ComponentModel.DataAnnotations;

namespace csharp_sol 
{
    public static class S271 
    {
        public static string Encode(IList<string> strs) 
        {
            string enc = "";
            foreach (string item in strs)
            {
                enc += $"{item.Length}#{item}";
            }

            return enc;
            
        }

        public static IList<string> Decode(string s) 
        {
            List<string> decoded = new List<string>();
            char[] chars = s.ToArray();
            int l = 0;
            string word;
            string count;
            while (l < s.Length)
            {
                word = "";
                count = "";

                while (chars[l] != '#')
                {
                    count += chars[l];
                    l++;
                }
                int count_i = Int32.Parse(count);
                l++;
                while (count_i > 0)
                {
                    word += chars[l];
                    count_i--;
                    l++;
                }

                decoded.Add(word);

            }

            return decoded;
            
        }
    }
}
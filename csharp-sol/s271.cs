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
            List<string> decoded = [];
            char[] chars = [.. s];
            int l = 0;
            while (l < s.Length)
            {
                string curr = "";
                while (chars[l] != '#' && l < s.Length-1)
                {
                    Console.WriteLine(l);
                    curr += chars[l];
                    l++;
                }
                Console.WriteLine(curr);

                l++;

            }

            return decoded;
            
        }
    }
}
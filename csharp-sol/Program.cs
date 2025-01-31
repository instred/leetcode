using System;

namespace csharp_sol
{
    public class Program
    {
        public static void Main(string[] args)
        {
            List<string> strs1 = ["Hello", "World"];
            List<string> strs2 = [""];
            List<string> strs3 = ["leet", "code", "is", "fun"];

            string encoded1 = S271.Encode(strs1);
            string encoded2 = S271.Encode(strs2);
            string encoded3 = S271.Encode(strs3);
            // Console.WriteLine(encoded1);
            // Console.WriteLine(encoded2);
            // Console.WriteLine(encoded3);

            Console.WriteLine(string.Join(", ", S271.Decode(encoded1)));
            Console.WriteLine(string.Join(", ", S271.Decode(encoded2)));
            Console.WriteLine(string.Join(", ", S271.Decode(encoded3)));
            
        }
    }
}
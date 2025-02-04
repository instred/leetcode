using System;

namespace csharp_sol
{
    public class Program
    {
        public static void Main(string[] args)
        {
            int[] nums1 = {1, 2, 3};
            int[] nums2 = {0};
            int[] nums3 = {1};
            S78 s78 = new();

            var result1 = s78.Subsets(nums1);
            var result2 = s78.Subsets(nums2);
            var result3 = s78.Subsets(nums3);

            foreach (var subset in result1) Console.WriteLine(string.Join(", ", subset));
            foreach (var subset in result2) Console.WriteLine(string.Join(", ", subset));
            foreach (var subset in result3) Console.WriteLine(string.Join(", ", subset));

        }
    }
}
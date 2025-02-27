using System;

namespace csharp_sol
{
    public class Program
    {
        public static void Main(string[] args)
        {
            int[] nums1 = {10, 20, 30, 5, 10, 50};
            int[] nums2 = {10, 20, 30, 40, 50};
            int[] nums3 = {12, 17, 15, 13, 10, 11, 12};

            Console.WriteLine(S1800.MaxAscendingSum(nums1));
            Console.WriteLine(S1800.MaxAscendingSum(nums2));
            Console.WriteLine(S1800.MaxAscendingSum(nums3));



        }
    }
}
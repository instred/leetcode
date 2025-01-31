using System.Collections.Generic;

namespace csharp_sol 
{
    public static class S217 
    {
        

        public static bool ContainsDuplicate(int[] nums) 
        {
            HashSet<int> hash_set = new(nums);
            
            return hash_set.Count != nums.Length;

        }
    }
}

namespace csharp_sol 
{
    public static class S1 
    {
        public static int[] TwoSum(int[] nums, int target) 
        {
            Dictionary<int, int> map = [];
            int[] ans = new int[2];
            for (int i=0; i < nums.Length; i++)
            {
                if (map.ContainsKey(target - nums[i]))
                {
                    ans[0] = map[target-nums[i]];
                    ans[1] = i;
                    return ans;
                }
                map[nums[i]] = i;
            }

            return ans;
            
        }
    }
}
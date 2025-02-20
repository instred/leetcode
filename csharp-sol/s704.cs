namespace csharp_sol 
{
    public static class S704 
    {
        public static int Search(int[] nums, int target) 
        {
            int l = 0;
            int r = nums.Length-1;
            
            while (l <= r)
            {
                int mid = (l+r) / 2;
                if (nums[mid] < target)
                {
                    l = mid+1;
                }
                else if (nums[mid] > target)
                {
                    r = mid-1;
                }
                else
                {
                    return mid;
                }

            }
            return -1;

        }
    }
}
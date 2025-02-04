namespace csharp_sol 
{
    public class S78 
    {
        List<IList<int>> res = [];
        public IList<IList<int>> Subsets(int[] nums) 
        {
            Backtrack(0, nums, new List<int>());
            return res;
        }
        private void Backtrack(int i, int[] nums, IList<int> subset)
        {
            if (i == nums.Length)
            {
                int[] curr = new int[subset.Count];
                subset.CopyTo(curr, 0);
                res.Add(curr);
                return;
            }

            subset.Add(nums[i]);
            Backtrack(i+1, nums, subset);
            subset.RemoveAt(subset.Count-1);
            Backtrack(i+1, nums, subset);
        }
    }
}
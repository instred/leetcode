namespace csharp_sol 
{
    public static class S347 
    {
        public static int[] TopKFrequent(int[] nums, int k) 
        {
            Dictionary<int, int> occ = [];
            List<int> ans = [];
            PriorityQueue<int, int> prio_q = new();

            foreach (int num in nums)
            {
                if (!occ.ContainsKey(num))
                {
                    occ[num] = 1;
                }
                else
                {
                    occ[num]++;
                }
            }
            foreach (var item in occ)
            {
                prio_q.Enqueue(item.Key, -item.Value);
            }
            while (k>0)
            {
                ans.Add(prio_q.Dequeue());
                k--;
            }

            return [.. ans];

        }
    }
}

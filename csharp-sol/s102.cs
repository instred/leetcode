namespace csharp_sol 
{

    public static class S102 
    {
        public static IList<IList<int>> LevelOrder(TreeNode root) 
        {
            if (root == null)
            {
                return [];
            }

            List<IList<int>> res = new();
            res.Add(new int[]{root.val});
            Queue<TreeNode> main_queue = new();
            Queue<TreeNode> level_que = new();
            main_queue.Enqueue(root);
            
            while (main_queue.Count != 0)
            {
                TreeNode curr = main_queue.Dequeue();
                
                if (curr.left != null)
                {
                    level_que.Enqueue(curr.left);
                }
                if (curr.right != null)
                {
                    level_que.Enqueue(curr.right);
                }

                if (main_queue.Count == 0)
                {
                    if (level_que.Count != 0)
                    {
                        IList<int> curr_level = [];
                        foreach (TreeNode node in level_que)
                        {
                            curr_level.Add(node.val);
                        }
                        res.Add(curr_level);
                        main_queue = level_que;
                        level_que = new();
                    }
                }
            }
            return res;
        }
    }
}
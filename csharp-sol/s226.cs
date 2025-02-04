namespace csharp_sol 
{
    public class TreeNode 
    {
        public int val;
        public TreeNode left;
        public TreeNode right;
        public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) 
        {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public static class S226 
    {
        public static TreeNode InvertTree(TreeNode root) 
        {
            if (root == null)
            {
                return root;
            }

            TreeNode left = root.left;
            TreeNode right = root.right;
            root.left = right;
            root.right = left;
            InvertTree(root.left);
            InvertTree(root.right);


            return root;
            
        }
    }
}
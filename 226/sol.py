from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def traverse(root):
            if not root:
                return 

            root.left, root.right = root.right, root.left
            if root.left:
                return traverse(root.left)
            
            if root.right:
                return traverse(root.right)
            
        traverse(root)
        return root



if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0)))
    print(sol.maxDepth(root))
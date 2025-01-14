from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diam = 0

        def dfs(root):
            nonlocal diam

            if not root:
                return 0
            
            lh = dfs(root.left)
            rh = dfs(root.right)
            d = lh + rh

            diam = max(diam, d)

            return 1+ max(lh, rh)

        dfs(root)
        return diam


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0)))
    print(sol.diameterOfBinaryTree(root))
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.isb = True

        def dfs(root):

            if not root:
                return 0
            
            lh = dfs(root.left)
            rh = dfs(root.right)
            # print(lh, rh)

            if abs(lh - rh) > 1:
                self.isb = False

            return 1 + max(lh, rh)
        
        dfs(root)
        return self.isb

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0, TreeNode(1))))
    print(sol.isBalanced(root))
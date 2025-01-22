from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, left, right):

            if not root:
                return True

            if not (left < root.val < right):
                return False
            

            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
        return dfs(root, float('-inf'), float('inf'))
    
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(2), TreeNode(9)))
    print(sol.isValidBST(root))
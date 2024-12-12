from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        l = self.inorderTraversal(root.left)
        r = self.inorderTraversal(root.right)
        return l + [root.val] + r

if __name__ == "__main__":
    tree = TreeNode(1,TreeNode(2), TreeNode(3, None, TreeNode(4)))
    s = Solution()
    print(s.inorderTraversal(tree))
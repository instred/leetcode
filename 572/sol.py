from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        tree = [root]

        while tree:
            curr = tree.pop()
            
            if curr.val == subRoot.val:
                print(curr, subRoot)
                if self.checkSame(curr, subRoot):
                    return True

            if curr.right:
                tree.append(curr.right)
            if curr.left:
                tree.append(curr.left)
        
        return False

    def checkSame(self, p, q):

        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.checkSame(p.left, q.left) and self.checkSame(p.right, q.right)

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0)))
    subRoot = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0)))
    print(sol.checkSame(root, subRoot))
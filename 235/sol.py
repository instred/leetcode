from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.lca = None
        def traverse(root, p, q):

            if p.val > q.val: p, q = q, p
            if p.val < root.val and q.val > root.val or p.val == root.val or q.val == root.val:
                self.lca = root
                return
            
            elif p.val < root.val and q.val < root.val:
                self.lowestCommonAncestor(root.left, p, q)

            else:
                self.lowestCommonAncestor(root.right, p, q)

        traverse(root, p, q)
        return self.lca




if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
    print(sol.lowestCommonAncestor(root, 2, 8))
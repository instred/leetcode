from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        idxs = {el : idx for idx, el in enumerate(inorder)}
        self.curr_preidx = 0

        def dfs(l, r):

            if l > r:
                return None
        
            val = preorder[self.curr_preidx]
            self.curr_preidx += 1

            root = TreeNode(val)
            mid = idxs[val]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)

            return root

        return dfs(0, len(preorder) - 1)


if __name__ == "__main__":
    sol = Solution()
    preorder = [3,9,20,15,7]  
    inorder = [9,3,15,20,7]  
    preorder2 = [-1]  
    inorder2 = [-1]
    print(sol.buildTree(preorder, inorder))
    print(sol.buildTree(preorder2, inorder2))
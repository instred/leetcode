from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(root, ans):
            stack = [root]
            while len(stack) > 0:
                curr = stack.pop()
                ans.append(curr.val)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                else:
                    ans.append(None)
            return ans
        
        if not p and not q: return True
        if not p or not q: return False

        ansp = dfs(p, [])
        ansq = dfs(q, [])
        
        return ansp == ansq
    
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        



if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2), TreeNode(3))
    s = Solution()
    print(s.isSameTree(tree, tree))
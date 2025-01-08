from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        else:
            ans = [[root.val]]
        que = deque([root])
        q = deque()
        while que:
            curr = que.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
           
            if not que:
                if q:
                    ans.append([x.val for x in q])
                    que = q
                    q = deque()

        return ans

    
r = TreeNode(5, TreeNode(3), TreeNode(7))
r.left.left = TreeNode(2)
r.left.right = TreeNode(4)
r.right.left = TreeNode (6)
r.right.right = TreeNode (8)

sol = Solution()
print(sol.levelOrder(r))
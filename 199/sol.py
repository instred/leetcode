from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        else:
            ans = [root.val]

        main_q = deque([root])
        level_q = deque()

        while main_q:
            curr = main_q.popleft()

            if curr.left:
                level_q.append(curr.left)
            if curr.right:
                level_q.append(curr.right)

            if not main_q:
                if level_q:
                    print(level_q)
                    ans.append(level_q[-1].val)
                    main_q = level_q
                    level_q = deque()

        return ans
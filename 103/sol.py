from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        else:
            ans = [[root.val]]
        que = deque([root])
        q = deque()
        i = 0
        while que:
            curr = que.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
           
            if not que:
                if q:
                    l = [x.val for x in q]
                    if i%2 == 0:
                        l.reverse()
                    i += 1
                    ans.append(l)
                    que = q
                    q = deque()

        return ans
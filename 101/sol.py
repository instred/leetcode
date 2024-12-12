from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.right and not root.left:
            return True

        if not root.left or not root.right:
            return False
        
        def isSame(root_left, root_right):
            if not root_left and not root_right:
                return True
            if not root_left or not root_right:
                return False
            if root_left.val != root_right.val:
                return False

            return isSame(root_left.left, root_right.right) and isSame(root_left.right, root_right.left)
        
        return isSame(root.left, root.right)
    

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.right and not root.left:
            return True
        if not root.left or not root.right:
            return False
        
        ansl, ansr = [], []
        stackl = [root.left]
        stackr = [root.right]
        while stackl:
            curr = stackl.pop()
            ansl.append(curr.val)
            if curr.left:
                stackl.append(curr.left)
            if curr.right:
                stackl.append(curr.right)
            else:
                ansl.append(None)
        
        while stackr:
            curr = stackr.pop()
            ansr.append(curr.val)
            if curr.right:
                stackr.append(curr.right)
            else:
                ansl.append(None)
            
            if curr.left:
                stackr.append(curr.left)
        print(ansl, ansr)

        return ansl == ansr


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = -1
        self.visited = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(root):
            if not root: return

            dfs(root.left)
            self.visited += 1
            if self.visited == k:
                self.ans = root.val
                return
            dfs(root.right)

        dfs(root)
        # print(self.visited, self.ans)
        return self.ans

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    print(sol.kthSmallest(root, 3))

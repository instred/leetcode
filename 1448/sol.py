class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.ans = 0

        def dfs(root, curr_max):
            if not root:
                return

            if curr_max <= root.val:
                self.ans += 1

            curr_max = max(root.val, curr_max)
            
            dfs(root.left, curr_max)
            dfs(root.right, curr_max)


        dfs(root, root.val)
        return self.ans




if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    print(sol.goodNodes(root))

        
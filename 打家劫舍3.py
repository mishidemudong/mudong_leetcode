


class Solution:
    def rob(self, root: TreeNode) -> int:

        def dfs(node):
            if node is None:
                return 0,0

            ls, lh = dfs(node.left)
            rs, rh = dfs(node.right)

            return node.val + lh + rh, max(ls + lh) + max(rs + rh)
        return max(dfs(root))
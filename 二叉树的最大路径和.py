

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):

        self.res = -999999
    def maxPathSum(self, root: TreeNode) -> int:


        #后续遍历框架
        def dfs(node):
            if node is None:
                return 0

            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            gain = node.val + left_gain + right_gain

            self.res = max(self.res, gain)

            ###这一步比较神奇
            return node.val + max(left_gain, right_gain)

        dfs(root)

        return self.res
'''


第一次题目一遍过，从审题到a c,都是一遍过，渐渐找到了刷题的乐趣啊。

1 叶子结点的定义，左右节点为None
2 先续遍历框架，同时是不是跟回溯的框架dfs有点像？

'''

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        result = []

        path_s = ''
        def dfs(node, path):
            if node is None:
                return
            else:
                path += str(node.val)

                if node.left is None and node.right is None:
                    result.append(path)

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, path_s)

        return sum([int(item) for item in result])
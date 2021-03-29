# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root, target):

    result, path = [], []

    def dfs(node, tar):
        if node is None:
            return

        path.append(node.val)
        tar -= node.val

        if tar == 0 and not node.left and not node.right:
            result.append(list(path))

        dfs(node.left, tar)
        dfs(node.right, tar)

        path.pop()

    dfs(root, target)

    return result






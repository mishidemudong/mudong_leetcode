
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # def incert_bst(node, val):
        #     if node is None:
        #         return TreeNode(val)
        #     if node.val == val:
        #         return node
        #     if node.val < val:
        #         node.right = incert_bst(node.right, val)
        #     elif node.val > val:
        #         node.left = incert_bst(node.left, val)
        #     return node

        # index = len(nums)//2
        # root = TreeNode(nums[index])
        # for val_ in nums[:index]:
        #     root.left = incert_bst(root, val_)

        # for val_ in nums[index+1:]:
        #     root.right = incert_bst(root, val_)

        # return root

        def preorder(left, right):
            if left > right:
                return None

            mid = (left +right) // 2

            root = TreeNode(nums[mid])
            root.left = preorder(left, mid -1)
            root.right = preorder(mid +1, right)

            return root

        return preorder(0, len(nums ) -1)


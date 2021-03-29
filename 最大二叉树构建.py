class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        if nums == []:
            return None


        max_num = max(nums)
        max_index = nums.index(max_num)

        root = TreeNode(max_num)

        ####注意list的左右边界问题，左闭右开
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index +1:])


        return root
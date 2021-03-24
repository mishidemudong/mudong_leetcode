# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findDuplicateSubtrees(root):
    res = []

    map_dict = {}

    def collect(node):
        if node == None:
            return '#'

        serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))

        if serial in map_dict.keys():
            map_dict[serial] += 1
        else:
            map_dict[serial]= 1

        if map_dict[serial] == 2:
            res.append(node)

    collect(root)

    return res





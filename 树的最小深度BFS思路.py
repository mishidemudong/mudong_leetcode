#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:18:18 2021

@author: liang
"""

'''
    叶子节点就是深度的最后一个节点，叶子节点的性质，左右子孩子为空
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = []
        queue.append(root)
        deepth = 1

        while queue != []:
            for i in range(len(queue)):
                cur = queue.pop()
                if cur.left is None and cur.right is None:
                    return deepth

                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)

            deepth += 1

        return deepth

    ####用DFS思路做，用递归
    def req_minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        deepth = 99999999


        if root.left:
            deepth = min(self.req_minDepth(root.left), deepth)

        if root.right:
            deepth = min(self.req_minDepth(root.right), deepth)

        return deepth + 1

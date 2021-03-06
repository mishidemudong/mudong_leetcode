#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 16:40:51 2021

@author: liang
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root, val):
    #找到空位置插入新节点
    if root == None:
        return TreeNode(val)

    if root.val == val:
        return root
    
    if root.val < val:
        root.right = insertIntoBST(root.right, val)
    
    elif root.val > val:
        root.left = insertIntoBST(root.left, val)
    
    return root
    
##先序遍历框架，也是快速排序的框架
def preorderBST(root):
    preorderlist = []

    if root is None:
        return
    preorderlist.append(root.val)

    '''
    快排：先选pivot,再去low,high 排序
    '''
    
    preorderBST(root.left)
    preorderBST(root.right)
    
    return preorderlist

#二叉搜索树的中续遍历是升序的数组#####
def midorderBST(root):
    midorderlist = []
    if root is None:
        return
    midorderBST(root.left)
    midorderlist.append(root.val)
    midorderBST(root.right)
    
    return midorderlist

    ##反向中续遍历，从大到小，第K大
    midorderlist = []
    index_ = 0
    if root is None:
        return
    midorderBST(root.right)
    midorderlist.append(root.val)
    if index_ == N:
        return node
    index_ += 1
    midorderBST(root.left)

    return midorderlist

##后序遍历框架，也是归并排序的框架
def postorderBST(root):
    postorderlist = []

    if root is None:
        return

    postorderBST(root.left)
    postorderBST(root.right)
    postorderlist.append(root.val)

    '''
    归并框架 merge
    '''
    return postorderlist

###层序遍历， 也是BFS的框架，比较重要的遍历方式
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = [[]]
        def level(node, levelc):

            if node is None:
                return
            else:
                result[levelc - 1].append(node.val)
                if len(result) == levelc:
                    result.append([])
                level(node.left, levelc + 1)
                level(node.right, levelc + 1)

        level(root, 1)

        return result

###层序遍历进阶，之字形遍历
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []
        result = [[]]
        def level_o(node, level):
            if node is None:
                return

            result[level - 1].append(node.val)
            if len(result) == level and (node.left or node.right):
                result.append([])

            if level % 2 == 0:
                level_o(node.left, level + 1)
                level_o(node.right, level + 1)
            else:
                level_o(node.right, level + 1)
                level_o(node.left, level + 1)

        level_o(root, 1)

        return result

###层序遍历进阶,
class Solution:
    def multiLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []
        result = []

        def level_o(node, level):
            if node is None:
                return
            if len(result) == level:
                result.append([])
            result[level].append(node.val)

            for subnode in node.children:
                level_o(subnode, level + 1)

        level_o(root, 0)

        return result

def createBST(vallist):
    if vallist == []:
        return None
    
    
    BSTTree = TreeNode(vallist[0])
    
    
    for val in vallist[1:]:
        BSTTree = insertIntoBST(BSTTree, val)
        
    return BSTTree

vallist = [5,3,6,2,4,7]

tree1 = createBST(vallist)

print()

##求完全二叉树的叶子数
###O(N)复杂度
def countNodes(root):
    if root == None:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)

import math
##满二叉树的计算
def countNodes(root):
    h = 0

    while root.left:
        root = root.left
        h += 1
    #节点总数就是 2^h - 1
    return math.pow(2, h) - 1


    return 1 + countNodes(root.left) + countNodes(root.right)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:18:18 2021

@author: liang
"""

'''
    1 用先序遍历和后续遍历二叉树都可以实现
    
    2 先序遍历：如果root在左右子树发现 p 和 q ，那么root
      后续遍历：如果p和q 的
      
    3 最后有3个情况
      1 左右都不为空，那么说明找到 返回root
      2 左右都为空，返回None
      3 左右哪个不为空，则返回谁
    
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):

    ###先序框架遍历二叉树
    # LCA 问题<br>        #利用先序遍历，寻找这两个节点
    if not root or root == p or root == q:  # 判断这三种情况，找到节点或者没有，若存在这个节点，则返回这个节点，若没有返回None
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    #找到root,以及左右两个节点，需要根据条件判断是否符合。
    # 1 左右都不为空，那么说明找到，返回root
    # 2 左右都为空，返回None
    # 3 左右哪个不为空，则返回谁
    if left is not None and right is not None:
        return root

    if left is None and left is None:
        return None

    if left is None:
        return right
    else:
        return left



s1 = "abcde"
s2 = "ace"

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
    

def preorderBST(root):
    preorderlist = []
    
    preorderlist.append(root.val)
    
    preorderBST(root.left)
    preorderBST(root.right)
    
    return preorderlist

def midorderBST(root):
    midorderlist = []

    midorderBST(root.left)
    midorderlist.append(root.val)
    midorderBST(root.right)
    
    return midorderlist

def postorderBST(root):
    postorderlist = []

    postorderBST(root.left)
    
    postorderBST(root.right)
    
    postorderlist.append(root.val)
    
    return postorderlist




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
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:17:35 2021

@author: Administrator
"""
'''
    说明：
    1 用先序遍历的框架，递归的套路是遍历交给框架，定义base case要做的事情。
    2 base case要做的事情是：按定义进行值相加，并且哪个左右子树不为空要补上。
    3 

'''

def mergeTrees(root1, root2):
    
    if root1 == None:
        return root2
    if root2 == None:
        return root1
    
    root1.val += root2.val
    
    root1.left = mergeTrees(root1.left, root2.left)
    root1.right = mergeTrees(root1.right, root2.right)
    
    
    return root1
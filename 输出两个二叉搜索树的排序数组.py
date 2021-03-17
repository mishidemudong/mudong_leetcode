# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:47:48 2021

@author: Administrator
"""

def getAllElements(root1, root2):
    
    def inorder(root):
        array = []
        
        inorder(root.left)
        array.append(root.val)
        inorder(root.right)
        
        return array
        
    array1 = inorder(root1)
    array2 = inorder(root2)
    
    
    
    
    return sorted(array1 + array2)
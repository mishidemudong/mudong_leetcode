# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 15:23:53 2021

@author: Administrator
"""

def missingNumber(nums):
    
    return sum(list(range(0,len(nums)+1))) - sum(nums)
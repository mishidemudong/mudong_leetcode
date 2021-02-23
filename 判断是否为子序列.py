#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:18:18 2021

@author: liang
"""
'''
    几个关键点：
    1 两个指针分别指向两个字符串，i只有相等时才前进， j指针每一步都前进
    2 假设

'''

def isSubsequence(s, t):
    i,j = 0,0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1

        j += 1

    return i == len(s)


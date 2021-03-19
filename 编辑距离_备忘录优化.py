#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:13:04 2021

@author: liang
"""

def levenstenDistance(str1, str2):
    if str1 =='':
        return len(str2)
    if str2 =='':
        return len(str1)
    ##基本情形判断，其中只要有一个是空字符串，编辑距离为长度，插入操作。

    memo = {}

    def dp(i, j):
        if (i, j) in memo.keys(): #构建dp字典表，先查表，在表中则返回
            return memo[(i, j)]

        if i == -1:
            return j + 1
        if j == -1:
            return i + 1

        if str1[i] == str2[j]:
            memo[(i, j)] = dp(i-1, j-1)# 当前两个指针对的值相等，同时上移一位
        else:
            memo[(i, j)] = min(dp(i, j-1) + 1, #str2 插入情形，当前字符插入一位，距离加一。
                       dp(i-1, j) + 1, #str1 删除情形，当前字符删除，距离加一
                       dp(i-1, j - 1) + 1, #替换情形，距离加一
                       )

        return memo[(i, j)]

    return dp(len(str1)-1, len(str2)-1)

print(levenstenDistance("abc", "bd"))
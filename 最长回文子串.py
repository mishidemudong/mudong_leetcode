#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:18:18 2021

@author: liang
"""
'''
总体采用双指针的思路
一个指针用于遍历字符串
然后以每个字符为中心，向两边生长，找最大回文

时间复杂度  O（N2） 空间复杂度 O（1）
'''

###定义判断回文函数

def judgehuiwen(dst_string, left, right):

    while left > 0 and right < len(dst_string) and dst_string[left] == dst_string[right]:

        left -= 1
        right += 1

    return dst_string[left+1:right]

def longestPalindrome(s):
    longst_huiwen = ''
    for index in range(len(s)):
        huiwen1 = judgehuiwen(s, index, index)
        huiwen2 = judgehuiwen(s, index, index+1)

        if len(huiwen1) > len(longst_huiwen):
            longst_huiwen = huiwen1

        if len(huiwen2) > len(longst_huiwen):
            longst_huiwen = huiwen2

    return longst_huiwen


print(longestPalindrome("babad"))
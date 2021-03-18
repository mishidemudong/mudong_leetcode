#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:13:04 2020

@author: liang
"""
'''
 问题1：将数组排序成最小数字
 问题2：将数组排序成最大数字

'''


import functools


def minNumber(self, nums):
    def sort_rule(x, y):
        a, b = x + y, y + x
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

    strs = [str(num) for num in nums]
    strs.sort(key=functools.cmp_to_key(sort_rule))
    return ''.join(strs)


def maxNumber(self, nums):
    def sort_rule(x, y):
        b, a = x + y, y + x
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

    strs = [str(num) for num in nums]
    strs.sort(key=functools.cmp_to_key(sort_rule))
    return ''.join(strs)


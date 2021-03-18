#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:13:04 2020

@author: liang
"""
'''
 问题1：

'''


def validSubarrays(nums):
    res, s = 0, list()

    nums.append(float('-inf'))

    for i in range(len(nums)):
        while s and nums[s[-1]] > nums[i]:
            res += i - s.pop()
        s.append(i)
    return res, s

nums = [1,4,2,5,3]


# sub_num, result_array = validSubarrays(nums)
# print(sub_num)
# print(result_array)

def validSubarrays2(nums):
    res= [[]]
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            tmp = []
            if (nums[j] >= nums[i]):
                tmp.append(nums[i:j+1])
        res.append(tmp)
    return res, len(res)

result_array, sub_num  = validSubarrays2(nums)

print(sub_num)
print(result_array)



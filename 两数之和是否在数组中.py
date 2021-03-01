#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:16:13 2021

@author: liang
"""


def twoSum(nums, target):

    for index in range(len(nums)):
        x = target - nums[index]

        if x in nums:
            return [index, nums.index(x)]

        else:
            return None
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:18:18 2021

@author: liang
"""

'''
    输入：nums = [10,9,2,5,3,7,101,18]
    输出：4
    解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

    动态规划法：
        dp数组或状态转移表：

'''

def lengthOfLIS(nums) :

    if not nums:
        return 0

    dp = []
    for i in range(len(nums)):
        dp.append(1)

        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

##暴力解法,还有点问题，没有ac
def lengthOfLISbao(nums):

    if len(set(nums)) == 1:
        return 1

    result = []

    for i in range(len(nums)):
        tmp = [nums[i]]
        index = 0
        for j in range(i + 1, len(nums)):

            if nums[j] >= tmp[index]:
                tmp.append(nums[j])
                index += 1
        result.append(len(tmp))

    return max(result)
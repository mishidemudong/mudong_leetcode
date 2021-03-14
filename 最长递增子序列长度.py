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
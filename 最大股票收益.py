#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:18:18 2021

@author: liang
"""

'''
1 暴力法 ， 时间超时
2 一次遍历发可以

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # result = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] > prices[i]:
        #             result= max(result, prices[j] - prices[i])
        # return result


        min_price = 999999
        max_profit = 0
        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(min_price, price)
        return max_profit


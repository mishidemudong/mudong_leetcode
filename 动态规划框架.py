#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:16:13 2021

@author: liang
"""


def dp(m_arr, n_arr):
    m, n = len(m_arr), len(n_arr)

    dp = [[0] * n for _ in range(m)]

    ##正向遍历
    for i in range(m):
        for j in range(n):

    ##反向遍历
    for i in range(m - 1, ):
        for j in range(n - 1, ):

    ##斜向遍历
    for i in range(m - 1, ):
        for j in range(n - 1, ):
            ###状态转移方程
            dp[i][j] = 1
            # 通过dp的遍历方向：dp[i-1][j] ,dp[i-1][j-1], d[i][j-1],dp[i+1][j] ,dp[i+1][j+1], d[i][j+1] 来计算dp[i][j]
            if m_arr[j] == n_arr[j]:
                dp[i][j] = max(dp[i + 1][j + 1], dp[][])

            else:
                dp[i][j] = dp[i + 1][j]

    return dp[m - 1][n - 1]


array = []


def dp(m_arr):
    m = len(m_arr)

    table = [0] * m
    count = 0
    for i in range(m):
        for j in range(m - i, m):
            if m_arr[i] < m_arr[j]:
                count += 1
                table[i] = count
                array.append(m_arr[j])
            else:
                dp()

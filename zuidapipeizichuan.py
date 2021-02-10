#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:01:41 2020

@author: liang
"""



text1 = 'abeceeeex'
text2 = 'becex'

substr = []


####zuida pipei changdu
m , n = len(text1), len(text2)
dp = [0] * (n+1)
for i in range(0, m):
    cur = [0] * (n+1)
    for j in range(0, n):
        if text1[i] == text2[j]:
            cur[j+1] = dp[j] + 1
            substr.append(text1[i])
        else:
            cur[j+1] = max(cur[j], dp[j+1])
            
    dp = cur
        
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [0] * (n+1)
    for i in range(m):
        cur = [0] * (n+1)
        for j in range(n):
            if text1[i] == text2[j]:
                cur[j+1] = dp[j] + 1
            else:
                cur[j+1] = max(cur[j], dp[j+1])
        dp = cur
    return dp[-1]

r1 = longestCommonSubsequence(text1, text2)
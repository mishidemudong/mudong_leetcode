#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:18:18 2021

@author: liang
"""

'''
    输入: str1 = "abcde", str2 = "ace" 
    输出: 3  
    解释: 最长公共子序列是 "ace"，它的长度是 3
'''

def lcs_recursive(s1, s2):
    if s1 =='' or s2 =='':
        return 0
    len1 = len(s1)
    len2 = len(s2)
    
    def dp(i, j):
        
        if i==-1 or j==-1:
            return 0
        else:
            if s1[i] == s2[j]:
                return dp(i-1, j-1) + 1
            else:
                return max(dp(i-1, j),dp(i, j-1))
    
    return dp(len1-1, len2-1)


s1 = "abcde"
s2 = "ace"
#print(lcs_recursive(s1, s2))


def lcs_dp(s1, s2):
    if s1 =='' or s2 =='':
        return 0
    len1 = len(s1)
    len2 = len(s2)
    
    dp_table = [[0]*(len2+1) for i in range(len1+1)]
        
    for i in range(1,len1+1):
        for j in range(1, len2+1):
            if s1[i-1] == s2[j-1]:
                dp_table[i][j] = dp_table[i-1][j-1] +1
            else:
                dp_table[i][j] =  max(dp_table[i-1][j],dp_table[i][j-1])
                
    return dp_table[-1][-1],dp_table


s1 = "abcde"
s2 = "ace"
print(lcs_dp(s1, s2))
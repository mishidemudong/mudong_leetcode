# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:04:15 2021

@author: Administrator
"""

'''
输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"


    说明:
        1 用到最长公共子串方法
        2 总共所需的删除动作是 len(s1) + len(s2) - 2*lcs，即，s1删除到lcs的步数加上s2删除到lcs的步数。
'''


def minDistance(word1, word2):
    
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
                    
        return dp_table[-1][-1]
    
    return len(word1) + len(word2) - 2*lcs_dp(word1, word2)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:59:16 2020

@author: liang
"""

def LCS(string1,string2):
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1+1)] for j in range(len2+1)]
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if string2[i-1] == string1[j-1]:
                res[i][j] = res[i-1][j-1]+1
            else:
                res[i][j] = max(res[i-1][j],res[i][j-1])
    return res,res[-1][-1]
print(LCS("helloworld","loop"))
# 输出结果为：
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
 [0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2],
 [0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 3],
 [0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 3]], 3

 
def LCstring(string1,string2):
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1+1)] for j in range(len2+1)]
    result = 0
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if string2[i-1] == string1[j-1]:
                res[i][j] = res[i-1][j-1]+1
                result = max(result,res[i][j])  
    return result
print(LCstring("helloworld","loop"))

def lcs(x,y):
    d = [0] * (len(x) + 1)
    for i in range(0,len(d)):
        d[i] = [0] * (len(y) + 1)
 
    for i in range(1,len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i-1] == y[j-1]:
                d[i][j] = d[i-1][j-1] + 1
            else:
                d[i][j] = max(d[i-1][j],d[i][j-1])
    print (d)
 
def lcs_extend(x,y):
    d = [0] * (len(x) + 1)
    p = [0] * (len(x) + 1)
    for i in range(0,len(d)):
        d[i] = [0] * (len(y) + 1)
        p[i] = [0] * (len(y) + 1)
 
    for i in range(1,len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i-1] == y[j-1]:
                d[i][j] = d[i-1][j-1] + 1
                p[i][j] = 1
            elif d[i-1][j] > d[i][j-1]:
                d[i][j] = d[i-1][j]
                p[i][j] = 2
            else:
                d[i][j] = d[i][j-1]
                p[i][j] = 3
    print (d)
    print (p)
    lcs_print(x,y,len(x),len(y),p)
 
def lcs_print(x,y,lenX,lenY,p):
    if lenX == 0 or lenY == 0:
        return
    if p[lenX][lenY] == 1:
        lcs_print(x,y,lenX-1,lenY-1,p)
#        print (x[lenX-1])
    elif p[lenX][lenY] == 2:
        lcs_print(x,y,lenX-1,lenY,p)
    else:
        lcs_print(x,y,lenX,lenY-1,p)
 
x = 'abcdf'
y = 'abcdef'#facefff
lcs_extend(x,y)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:18:18 2021

@author: liang
"""

'''
说明：
    1 遇到左括号就入栈
    2 遇到右括号就去栈中寻找最近的左括号，看是否匹配。
    
注意Python的list 可以当栈用，top位置其实是最后一个元素位置
'''

def pipeikuohao(c):

    trans  = {")":"(", "]":"[", "}": "{"}

    return trans[c]


def isValid(s):
    data = []

    for char in s:
        if char in ["(", "{", "["]:
            data.append(char)
            # print("push",data)
        else:
            if not len(data)==0 and pipeikuohao(char) == data[-1]:
                data.pop()
            else:
                return False

    return True if len(data)==0 else False

print(isValid("{[]}"))
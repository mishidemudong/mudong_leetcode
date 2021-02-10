#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 17:05:21 2020

@author: liang
"""

def reverseWords(s: str) -> str:
    
    a = s.split(' ')
    a.reverse()
    return ' '.join(a)


print(reverseWords("the sky is blue"))


#a = s.split(' ')
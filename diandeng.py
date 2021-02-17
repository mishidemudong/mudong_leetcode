#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 19:13:59 2020

@author: liang
"""
'''
本质是找规律，然后用循环，递归，数学等公式描述出来就OK了。

'''
import math

def bulbSwitch(n):
    
    return int(math.sqrt(n))


a1 = bulbSwitch(1000)
print(a1)

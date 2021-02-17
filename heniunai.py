#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:16:13 2021

@author: liang
"""
'''
这类问题的实质就是 找规律，然后通过循环，递归等方式实现

'''



def heniunai(N):
    money = 0
    if N==0:
        return 0
    elif N <=2 and N >=1:
        money += N*5
        return money
    else:
        
        if N % 2 ==0:
            money += 5 + heniunai(N-1)            
        else:
            money += 1 + heniunai(N-1)
        
    return money


for i in range(9):
    print(heniunai(i))
    
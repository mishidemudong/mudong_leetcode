#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:18:02 2020

@author: liang
"""


sorted_array = [1,2,3,4,5,6,7,8,9]
rotated_array = [7,8,9,1,2,3,4,5,6]


left=0
right = len(sorted_array)-1


destvalue = 3

while left < right:
    mid = (left + right) // 2
    if destvalue == sorted_array[mid]:
        print(mid)
        break
    elif destvalue > sorted_array[mid]:
        left = mid
    else:
        right = mid
        
minvalue = rotated_array[0]
left=0
right = len(rotated_array)-1
while left < right:
    mid = (left + right) // 2
    if minvalue > rotated_array[mid]:
        left = mid
        minvalue = rotated_array[mid]
    else:
        right = mid
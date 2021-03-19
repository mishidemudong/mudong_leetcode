#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:18:18 2021

@author: liang
"""

import itertools

class Solution:
    def permutation(self, s: str):
        result=set()
        for i in itertools.permutations(s):
            string=''.join(i)
            result.add(string)
        return list(result)

def permute(nums):

    result = []

    def backtrack(path, choose_list):
        if choose_list==[]:
            # result.append(path[:])
            # print(type(path)) #path[:]和path的区别：[:]是path的深拷贝！！！！
            result.append(path[:])
            return

        for item in choose_list:
            # print("item", item)
            path.append(item)
            backtrack(path, choose_list[:choose_list.index(item)] + choose_list[choose_list.index(item)+1:])

            path.pop()

        ###原始方法，删除和恢复
        for item in choose_list:
            # print("item", item)
            path.append(item)
            index_ = choose_list.index(item)
            choose_list.remove(item)
            backtrack(path, choose_list)
            choose_list.insert(index_,item)
            path.pop()


    backtrack([], nums)

    return result

a = [1,2,3]
print(permute(a))
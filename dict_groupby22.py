#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 21:20:10 2020

@author: liang
"""

from operator import itemgetter # itemgetter用来去dict中的key，省去了使用lambda函数
from itertools import groupby # itertool
d1={'name':'zhangsan','age':20,'country':'China'}
d2={'name':'wangwu','age':19,'country':'USA'}
d3={'name':'lisi','age':22,'country':'JP'}
d4={'name':'zhaoliu','age':22,'country':'USA'}
d5={'name':'pengqi','age':22,'country':'USA'}
d6={'name':'lijiu','age':22,'country':'China'}
lst=[d1,d2,d3,d4,d5,d6]

# 通过country进行分组：
lst.sort(key=itemgetter('country')) # 需要先排序，然后才能使用groupby
lstg = groupby(lst,itemgetter('country')) # 分组
# 等同于lstg = groupby(lst,key=lambda x:x['country'])
for country,items in lstg:
    print(country,list(items))
    # for item in items:
    #     print(item)
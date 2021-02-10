#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:01:28 2020

@author: liang
"""

data = [
        {"issue_id": 11, "date": "2020-02-02", "num": 1},
        {"issue_id": 11, "date": "2020-02-03", "num": 1},
        {"issue_id": 22, "date": "2020-02-04", "num": 2},
        {"issue_id": 22, "date": "2020-02-02", "num": 2},
        {"issue_id": 33, "date": "2020-02-04", "num": 3},
        {"issue_id": 33, "date": "2020-02-02", "num": 3},
       ]
 
 
def key_sort_group(data):
    """对列表中dict数据指定key排序，分组"""
    # 排序
    from operator import itemgetter
    from itertools import groupby
    data.sort(key=itemgetter('issue_id'))   # issue_id排序；无返回值
    result = dict()
    for issue_id, items in groupby(data, key=itemgetter('issue_id')):  # 按照issue_id分组
        result[str(issue_id)] = list(items)
    return result
    
ret = key_sort_group(data)

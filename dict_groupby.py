#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on Thu Jun 18 15:00:22 2020

@author:liang
"""

data=[
　　{'id':'078af4a6228047dba0', 'main_code':'TJ', 'code':'XC001', 'groupid':0, 'column_name':'name', 'column_value':'张三'},
  
　　{'id':'078af4a6228047dba0', 'main_code':'TJ', 'code':'XC001', 'groupid':0, 'column_name':'age', 'column_value':'27'},

　　{'id':'078af4a6228047dba0', 'main_code':'TJ','code':'XC001','groupid':1,'column_name':'name','column_value':'李四'},

　　{'id':'078af4a6228047dba0', 'main_code':'TJ','code':'XC001','groupid':1,'column_name':'age','column_value':'45'},

　　{'id':'078af4a6228047dba0', 'main_code':'LP', 'code':'XC001', 'groupid':0, 'column_name':'name', 'column_value':'张三'},

　　{'id':'078af4a6228047dba0', 'main_code':'LP', 'code':'XC001', 'groupid':0, 'column_name':'age', 'column_value':'27'},

　　{'id':'078af4a6228047dba0', 'main_code':'LP','code':'XC001','groupid':1,'column_name':'name','column_value':'李四'},

　　{'id':'078af4a6228047dba0', 'main_code':'LP','code':'XC001','groupid':1,'column_name':'age','column_value':'45'},

　　{'id':'078af4a6228047dba0', 'main_code':'TJ','code':'RY002','groupid':0,'column_name':'sex','column_value':'男'},

　　{'id':'82970de3e3b836d34', 'main_code':'TJ','code':'BD001','groupid':0,'column_name':'isEnable','column_value':True}

]

from operator import itemgetter
from itertools import groupby
import json
data.sort(key=itemgetter('id'))
datas = []
# id分组
for id, items in groupby(data, key=itemgetter('id')):
    data_dict = {'id':id}
    for code_info, item in groupby(items, key=itemgetter('main_code','code')):
        if code_info[0]:
            column=[]
            list_item=[i for i in item]
            list_item.sort(key=itemgetter('groupid'))
            for group_id,g_item in groupby(list_item,key=itemgetter('groupid')):
                column_dict = {}
                for gi in g_item:
                    column_dict[gi.get('column_name')] = gi.get('column_value')
                column_dict['group_id'] = group_id
                column.append(column_dict)
                data_dict[f'{code_info[0]}{code_info[1]}'] = column if len(column)>1 else column[0]
        else:
            data_dict[f'{code_info[0]}{code_info[1]}'] = '无数据'
    datas.append(data_dict)
print(json.dumps(datas,ensure_ascii=False))
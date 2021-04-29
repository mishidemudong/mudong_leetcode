
'''
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:
输入:
"tree"

输出:
"eert"

解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。

'''

class Solution:
    def frequencySort(self, s: str) -> str:
        map_dict = {}
        for char in s:
            if char in map_dict.keys():
                map_dict[char] += 1
            else:
                map_dict[char] = 1

        map_dict = sorted(map_dict.items(), key=lambda x:x[1],reverse=True)

        return ''.join([''.join([x[0]]*x[1]) for x in map_dict])
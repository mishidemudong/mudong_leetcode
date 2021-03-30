
'''
在DFS排列组合字符串的基础上改的，虽然ac了，但效率比较低
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        new_nums = [str(item) + '_' + str(i) for i, item in  enumerate(nums)]
        # print(new_nums)
        result = set()

        def dfs(path, choose_list):
            if choose_list == []:
                res = '*'.join(item.split('_')[0] for item in  path[:])
                # print(res)
                result.add(res)
                return

            for item in choose_list:
                path.append(item)
                index_item = choose_list.index(item)
                choose_list.remove(item)
                dfs(path, choose_list)
                path.pop()
                choose_list.insert(index_item,item)

        dfs([],new_nums)

        return [[eval(item) for item in x.split('*') ] for x in list(result)]


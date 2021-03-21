



result = []
def backtrack(path, choose_选择_list):


    ###满足结束条件时，记录路径
    if len(path) == len(choose_选择_list):
        path = path[:]
        #或者path = deepcopy(path)
        result.append(path)

    #核心框架，根据choose_选择_list 做选择

    for choose in choose_选择_list:
        #做选择

        #更新选择list和path
        choose_index = choose_选择_list.index(choose_index)
        new_choose_选择_list = choose_选择_list - choose

        path_index = path.index(choose)
        path.append(choose)

        backtrack(path, new_choose_选择_list)

        ##撤销选择
        ##恢复路径和选择列表

        path.pop(path_index)
        choose_选择_list.incert(choose, choose_index)

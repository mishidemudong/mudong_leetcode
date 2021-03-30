



'''
纯暴力解法

'''

a = [1,2,3,1,2,1,5,4]

s = 7

def func(array, target):

    result = []
    dp = [0] * (len(array))

    for i in range(0, len(array)-1):
        for j in range(i+1, len(array)+1):

            if sum(array[i:j]) > target:
               result.append(j-i)

    return min(result)

print(func(a, s))


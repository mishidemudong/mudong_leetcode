
char = ['h','e','l','o']


def exchange(array):

    i = 0
    j = len(array)-1

    while i < j:
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp
        i+=1
        j-=1
    return array

print(exchange(char))
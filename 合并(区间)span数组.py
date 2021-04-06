

example = [(2, 5), (7, 9), (3, 9), (14, 20)]
example = sorted(example, key=lambda x: x[0], reverse=False)

new_array = []
i = 1
while i < len(example):
    start = example[i - 1][0]
    end = example[i - 1][1]
    while i < len(example) and example[i][0] <= example[i - 1][1]:
        end = max(example[i][1], end)
        i += 1
    new_array.append((start, end))
    i += 1

###
if i == len(example) and example[-1][0] <= new_array[-1][1]:
    new_array[-1][1] = example[-1][1]
else:
    new_array.append(example[-1])

print(new_array)


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # 如果列表为空，或者当前区间与上一区间不重合，直接添加
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # 否则的话，我们就可以与上一区间进行合并
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

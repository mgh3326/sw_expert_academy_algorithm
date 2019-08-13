# TestCase Number Input
import itertools


def perm(a):
    length = len(a)
    if length == 1:
        return [a]
    else:
        result = []
        for i in a:
            b = a.copy()
            b.remove(i)
            b.sort()
            for j in perm(b):
                j.insert(0, i)
                if j not in result:
                    result.append(j)
        return result


my_list = []
size = 3
for _size in range(size):
    temp_list = []

    for i in range(size):
        temp_list.append(i)
    my_list.append(temp_list)
for _size in range((size - 1) * (size - 1)):
    for i in range(2):
        print(_size, i)

right_index = 0
down_index = 0
result = perm([1, 1, 2, 2])
print(result)
# print(my_list)

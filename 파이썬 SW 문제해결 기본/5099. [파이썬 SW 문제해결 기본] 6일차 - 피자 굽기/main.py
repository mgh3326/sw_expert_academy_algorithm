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


# TestCase Number Input
test_case_num = int(input())
for test_case_index in range(test_case_num):
    size = int(input())
    num_list = []
    current_count = 0
    for _size in range(size):
        temp_list = list(map(int, input().split()))
        num_list.append(temp_list)
    perm_list = []
    for i in range(size - 1):
        perm_list.append(0)
        perm_list.append(1)
    perm_list = perm(perm_list)

    for perm_index in perm_list:
        temp = 0
        right_index = 0
        down_index = 0
        for index in perm_index:
            if index == 0:
                right_index += 1
            else:
                down_index += 1
            temp += num_list[right_index][down_index]
            if current_count != 0 and temp > current_count:
                break

        if current_count == 0 or temp < current_count:
            current_count = temp

    current_count += num_list[0][0]

    print("#%d %d" % (test_case_index + 1, current_count))

    # print output

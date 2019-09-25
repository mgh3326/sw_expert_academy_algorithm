test_case_num = 10
array_size = 100
for _ in range(test_case_num):
    test_case_index = int(input())
    arr_list = []
    current_count = 0
    for _ in range(array_size):
        temp_list = list(map(int, input().split()))
        _sum = sum(temp_list)  # 가로 합
        if current_count == 0 or (_sum > current_count):
            current_count = _sum
        arr_list.append(temp_list)
    temp1 = 0
    temp2 = 0
    for i in range(array_size):
        temp1 += arr_list[i][i]
        temp2 += arr_list[array_size - i - 1][i]
        temp = 0
        for j in range(array_size):
            temp += arr_list[j][i]
        if temp > current_count:
            current_count = temp
    if temp1 > current_count:
        current_count = temp1
    if temp2 > current_count:
        current_count = temp2

    print("#%d %d" % (test_case_index, current_count))

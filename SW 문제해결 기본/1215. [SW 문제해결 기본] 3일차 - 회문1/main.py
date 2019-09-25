test_case_num = 10
arr_size = 8
for test_case_index in range(10):
    arr_list = []
    str_length = int(input())
    current_count = 0
    for i in range(arr_size):
        temp_list = input()
        arr_list.append(temp_list)
    for i in range(arr_size):
        for j in range(arr_size - str_length + 1):
            temp_str = arr_list[i][j:j + str_length]
            for _l in range(str_length // 2):
                if temp_str[_l] != temp_str[str_length - _l - 1]:
                    break
                if _l == (str_length // 2) - 1:
                    current_count += 1
        for j in range(arr_size - str_length + 1):
            temp_str = ""
            for k in range(str_length):
                temp_str += arr_list[j + k][i]
            for _l in range(str_length // 2):
                if temp_str[_l] != temp_str[str_length - _l - 1]:
                    break
                if _l == (str_length // 2) - 1:
                    current_count += 1

    print("#%d %d" % (test_case_index + 1, current_count))

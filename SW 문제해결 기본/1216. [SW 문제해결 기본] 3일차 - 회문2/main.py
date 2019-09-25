test_case_num = 10
arr_size = 100
for test_case_index in range(10):
    arr_list = []
    test_case_index_number = int(input())
    current_count = 0
    is_end = False
    for _ in range(arr_size):
        temp_list = input()
        arr_list.append(temp_list)
    for str_length in reversed(range(1, arr_size + 1)):
        if is_end:
            break
        if str_length == 1:
            current_count = 1
            break

        for i in range(arr_size):
            if is_end:
                break
            for j in range(arr_size - str_length + 1):
                if is_end:
                    break
                temp_str = arr_list[i][j:j + str_length]
                for _l in range(str_length // 2):
                    if temp_str[_l] != temp_str[str_length - _l - 1]:
                        break
                    if _l == (str_length // 2) - 1:
                        current_count = str_length
                        is_end = True
            for j in range(arr_size - str_length + 1):
                if is_end:
                    break
                temp_str = ""
                for k in range(str_length):
                    temp_str += arr_list[j + k][i]
                for _l in range(str_length // 2):
                    if temp_str[_l] != temp_str[str_length - _l - 1]:
                        break
                    if _l == (str_length // 2) - 1:
                        current_count = str_length
                        is_end = True

    print("#%d %d" % (test_case_index_number, current_count))

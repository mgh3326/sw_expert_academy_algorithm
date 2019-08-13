test_case_num = 10
arr_size = 100
for test_case_num_i in range(test_case_num):
    test_case_index = int(input())
    arr_list = []
    for i in range(arr_size):
        temp_list = list(map(int, input().split()))
        arr_list.append(temp_list)
    goal_index = arr_list[arr_size - 1].index(2)
    current_index = arr_size - 1
    while True:

        if goal_index == 0:
            if arr_list[current_index][goal_index + 1] == 1:
                while True:
                    if arr_list[current_index][goal_index + 1] == 1:
                        goal_index += 1

                    else:
                        break
                current_index -= 1
            else:
                current_index -= 1
        elif goal_index == arr_size - 1:
            if arr_list[current_index][goal_index - 1] == 1:
                while True:
                    if arr_list[current_index][goal_index - 1] == 1:
                        goal_index -= 1
                        if goal_index == 0:
                            break
                    else:
                        break
                current_index -= 1
            else:
                current_index -= 1

        else:
            if arr_list[current_index][goal_index + 1] == 1:
                while True:

                    if arr_list[current_index][goal_index + 1] == 1:
                        goal_index += 1
                        if goal_index == 99 or goal_index == 0:
                            break
                    else:
                        break
                current_index -= 1

            elif arr_list[current_index][goal_index - 1] == 1:
                while True:
                    if arr_list[current_index][goal_index - 1] == 1:
                        goal_index -= 1
                    else:
                        break
                current_index -= 1
            else:
                current_index -= 1
        if current_index == 0:
            break

    # 왼쪽 혹은 오른쪽이 1인지
    print("#%d %d" % (test_case_index, goal_index))

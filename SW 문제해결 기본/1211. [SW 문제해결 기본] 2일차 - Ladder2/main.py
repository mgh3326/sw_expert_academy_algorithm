test_case_num = 10
arr_size = 100
for test_case_num_i in range(test_case_num):
    test_case_index = int(input())
    min_count = 0
    arr_list = []
    min_count_start_point = 0
    for i in range(arr_size):
        temp_list = list(map(int, input().split()))
        arr_list.append(temp_list)
    for horizontal_index in reversed(range(arr_size)):
        vertical_index = 0

        if arr_list[vertical_index][horizontal_index] == 0:  # 이러면 출발도 안 해
            continue
        vertical_index += 1
        current_count = 1  # 한칸 내려오고 시작해도 될것같다
        loop_horizontal_index = horizontal_index

        while True:
            if loop_horizontal_index == 0:
                if arr_list[vertical_index][loop_horizontal_index + 1] == 1:
                    while True:
                        if loop_horizontal_index == arr_size - 1:
                            break
                        if arr_list[vertical_index][loop_horizontal_index + 1] == 1:
                            current_count += 1
                            loop_horizontal_index += 1
                        else:
                            break
                    current_count += 1
                    vertical_index += 1
                else:
                    current_count += 1
                    vertical_index += 1
            elif loop_horizontal_index == arr_size - 1:
                if arr_list[vertical_index][loop_horizontal_index - 1] == 1:
                    while True:

                        if loop_horizontal_index == 0:
                            current_count += 1
                            break
                        if arr_list[vertical_index][loop_horizontal_index - 1] == 1:
                            current_count += 1
                            loop_horizontal_index -= 1
                        else:
                            break
                    current_count += 1
                    vertical_index += 1
                else:
                    current_count += 1
                    vertical_index += 1

            else:
                if arr_list[vertical_index][loop_horizontal_index + 1] == 1:
                    while True:
                        if loop_horizontal_index == arr_size - 1:
                            break
                        if arr_list[vertical_index][loop_horizontal_index + 1] == 1:
                            current_count += 1
                            loop_horizontal_index += 1
                        else:
                            break
                    current_count += 1
                    vertical_index += 1
                elif arr_list[vertical_index][loop_horizontal_index - 1] == 1:
                    while True:
                        if loop_horizontal_index == 0:
                            break
                        if arr_list[vertical_index][loop_horizontal_index - 1] == 1:
                            current_count += 1
                            loop_horizontal_index -= 1
                        else:
                            break
                    current_count += 1
                    vertical_index += 1
                else:
                    current_count += 1
                    vertical_index += 1

            if vertical_index == arr_size - 1:
                break

        # While 문 끝
        if min_count == 0 or min_count > current_count:
            min_count = current_count
            min_count_start_point = horizontal_index

    # 왼쪽 혹은 오른쪽이 1인지
    print("#%d %d" % (test_case_index, min_count_start_point))

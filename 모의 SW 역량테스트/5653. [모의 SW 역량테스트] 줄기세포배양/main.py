dx = [1, 0, -1, 0]  # Right, down, left, up
dy = [0, 1, 0, -1]


def grow_cells():
    global my_list
    global result
    if len(saved_remove_list) != 0:
        result -= saved_remove_list[0]
        for saved_remove_list_index in range(len(saved_remove_list) - 1):
            saved_remove_list[saved_remove_list_index] = saved_remove_list[saved_remove_list_index + 1]
        saved_remove_list[-1] = 0

    for cell in reversed(cell_list):

        if len(cell) == 0:
            continue
        remove_list = []
        temp_cell_list = []
        cell_index = cell_list.index(cell)
        for idx, c in enumerate(cell):

            c[1] -= 1
            if c[1] == -1:  # 세포 배양 시작
                remove_list.append(idx)
                # 이거 나중에는 지워도 되겠다.
                for dir_idx in range(4):
                    nx, ny = dx[dir_idx], dy[dir_idx]
                    current_h = c[0][0] + ny
                    current_w = c[0][1] + nx
                    value = my_list[current_h][current_w]
                    if value == 0:  # 세포 증식
                        my_list[current_h][current_w] = cell_index
                        temp_cell_list.append(
                            [
                                [current_h, current_w], cell_index
                            ]
                        )
                        result += 1
        for remove in reversed(remove_list):
            cell.remove(cell[remove])
            if cell_index == 1:
                result -= 1
            else:
                saved_remove_list[cell_index - 2] += 1
        for temp_cell in temp_cell_list:
            cell.append(temp_cell)


# TODO 재민욱찡이랑 내가 뭐가 다른지 비교해보도록 하자
test_case_num = int(input())
for test_case_index in range(test_case_num):
    n, m, k = map(int, input().split())
    my_k = k // 2
    count = 0
    # 입력의 첫 번째 줄은 배열의 행 수입니다.
    result = 0
    my_list = []
    cell_list = []
    for i in range(2 * my_k + n):
        my_list.append([0] * (2 * my_k + m))

    for i in range(n):
        temp_list = list(map(int, input().split()))
        for temp_index in range(len(temp_list)):
            if temp_list[temp_index] != 0:
                result += 1
                try:
                    cell_list[temp_list[temp_index]].append([
                        (my_k + i, my_k + temp_index),
                        temp_list[temp_index]
                    ])
                except IndexError:
                    for _i in range(len(cell_list), temp_list[temp_index] + 1):
                        cell_list.append([])
                    cell_list[temp_list[temp_index]].append([
                        (my_k + i, my_k + temp_index),
                        temp_list[temp_index]
                    ])
            my_list[my_k + i][my_k + temp_index] = temp_list[temp_index]
    saved_remove_list = [0] * (len(cell_list) - 2)

    for k_index in range(k):
        # print(k_index)
        # for _map in my_list:
        #     print(_map)
        grow_cells()
    print("#%d %d" % (test_case_index + 1, result))

dx = [1, 0, -1, 0]  # Right, down, left, up
dy = [0, 1, 0, -1]
is_cutting = False


def double_list_get_list(_input: list, position: list):
    return _input[position[0]][position[1]]


def grow_cells():
    global map_list
    global result
    for cell in reversed(cell_list):

        if len(cell) == 0:
            continue
        remove_list = []
        temp_cell_list = []
        cell_index = cell_list.index(cell)
        for idx, c in enumerate(cell):

            c[1] -= 1
            if c[1] == -1:
                remove_list.append(idx)
                for dir_idx in range(4):
                    nx, ny = dx[dir_idx], dy[dir_idx]
                    current_h = c[0][0] + ny
                    current_w = c[0][1] + nx
                    value = map_list[current_h][current_w]
                    if value == 0:
                        map_list[current_h][current_w] = cell_index
                        temp_cell_list.append(
                            [
                                [current_h, current_w], cell_index
                            ]
                        )
                        result += 1
        for remove in reversed(remove_list):
            cell.remove(cell[remove])
            result -= 1
        for temp_cell in temp_cell_list:
            cell.append(temp_cell)


test_case_num = int(input())
for test_case_index in range(test_case_num):
    n, m, k = map(int, input().split())
    count = 0
    # 입력의 첫 번째 줄은 배열의 행 수입니다.
    result = 0
    map_list = []
    for i in range(2 * k + n):
        map_list.append([0] * (2 * k + m))
    cell_list = []

    for i in range(n):
        temp_list = list(map(int, input().split()))
        for temp_index in range(len(temp_list)):
            if temp_list[temp_index] != 0:
                result += 1
                try:
                    cell_list[temp_list[temp_index]].append([
                        (k + i, k + temp_index),
                        temp_list[temp_index]
                    ])
                except IndexError:
                    for _i in range(len(cell_list), temp_list[temp_index] + 1):
                        cell_list.append([])
                    cell_list[temp_list[temp_index]].append([
                        (k + i, k + temp_index),
                        temp_list[temp_index]
                    ])
            map_list[k + i][k + temp_index] = temp_list[temp_index]
    for k_index in range(k):
        print(k_index)
        for _map in map_list:
            print(_map)
        grow_cells()
    print("#%d %d" % (test_case_index + 1, result))

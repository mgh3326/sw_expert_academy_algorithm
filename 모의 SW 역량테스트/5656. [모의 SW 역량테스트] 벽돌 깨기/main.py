import copy

dx = [1, 0, -1, 0]  # Right, down, left, up
dy = [0, 1, 0, -1]
is_cutting = False


def temp_sum(input_list):
    count = 0
    for _i in input_list:
        for __i in _i:
            if __i != 0:
                count += 1
    return count


def double_list_get_list(_input: list, position: list):
    return _input[position[0]][position[1]]


def breaking_brick(point: list, input_list: list):
    global temp_dict
    global current_result
    value = double_list_get_list(input_list, point)
    if value == 0:
        return
    if value not in temp_dict:
        temp_dict[value] = []
    temp_dict[value].append(point)
    input_list[point[0]][point[1]] = 0
    current_result -= 1

    for dir_idx in range(len(dx)):
        # temp_removed_list = []

        nx, ny = dx[dir_idx], dy[dir_idx]
        for value_index in range(1, value):
            new_point_h = point[0] + ny * value_index
            new_point_w = point[1] + nx * value_index
            if new_point_w >= w or new_point_w < 0 or new_point_h < 0 or new_point_h >= h:
                continue
            new_point = [new_point_h, new_point_w]
            new_value = double_list_get_list(input_list, new_point)
            breaking_brick(new_point, input_list)
        # removed_list.append(temp_removed_list)


def find_top_level(w_pram, input_list: list):
    for _h_index in range(h):
        if input_list[_h_index][w_pram] != 0:
            return _h_index
    return -1


def shout_dfs(depth: int, input_list):
    global check_list
    global min_result

    if depth >= n - 1:
        return
    copy_list = copy.deepcopy(input_list)
    # list 당기기
    for w_index in range(w):
        h_index = find_top_level(w_index, copy_list)
        for _h_index in range(h_index + 1, h):
            if copy_list[_h_index][w_index] == 0:
                for __h_index in reversed(range(h_index, _h_index)):
                    copy_list[__h_index + 1][w_index] = copy_list[__h_index][w_index]
                copy_list[h_index][w_index] = 0

    for w_index in range(w):
        global temp_dict
        global current_result
        h_index = find_top_level(w_index, copy_list)
        if h_index != -1:
            temp_dict = {}
            breaking_brick([h_index, w_index], copy_list)
            if min_result > current_result:
                min_result = current_result
            removed_list.append(temp_dict)
        else:
            continue
        shout_dfs(depth + 1, copy_list)
        removed_list_pop = removed_list.pop()
        for _removed_list in removed_list_pop:
            for _temp in removed_list_pop[_removed_list]:
                copy_list[_temp[0]][_temp[1]] = _removed_list
                current_result += 1

        # 벽돌 복구


test_case_num = int(input())
for test_case_index in range(test_case_num):
    n, w, h = map(int, input().split())
    # 입력의 첫 번째 줄은 배열의 행 수입니다.
    my_list = []
    check_list = []
    removed_list = []

    current_result = 0
    saved_result = 0
    for i in range(n):
        check_list.append([False] * 10)

    for i in range(h):
        temp_list = list(map(int, input().split()))
        for temp in temp_list:
            if temp != 0:
                current_result += 1
        my_list.append(temp_list)
    min_result = current_result
    shout_dfs(depth=-1, input_list=my_list)

    print("#%d %d" % (test_case_index + 1, min_result))

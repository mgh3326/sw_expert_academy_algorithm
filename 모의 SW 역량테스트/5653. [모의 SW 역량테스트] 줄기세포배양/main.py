dx = [1, 0, -1, 0]  # Right, down, left, up
dy = [0, 1, 0, -1]
is_cutting = False


def double_list_get_list(_input: list, position: list):
    return _input[position[0]][position[1]]


def check_map(dir_idx: int, _peak: list):
    global map_list
    global result
    global max_result
    global is_cutting
    nx, ny = dx[dir_idx], dy[dir_idx]
    peak_value = map_list[_peak[0]][_peak[1]][0]
    origin_peak = _peak.copy()
    _peak[0] = _peak[0] + ny
    _peak[1] = _peak[1] + nx
    if 0 <= _peak[1] < n and 0 <= _peak[0] < n:
        if map_list[_peak[0]][_peak[1]][1] == False:
            if peak_value > map_list[_peak[0]][_peak[1]][0]:

                map_list[_peak[0]][_peak[1]][1] = True
                result += 1
                if max_result < result:
                    max_result = result
                return True
            else:
                if is_cutting == False:
                    var_value = map_list[_peak[0]][_peak[1]][0] - peak_value
                    for cutting_value in range(var_value + 1, k + 1):
                        is_cutting = True
                        map_list[_peak[0]][_peak[1]][0] -= cutting_value
                        map_list[_peak[0]][_peak[1]][1] = True
                        result += 1
                        if max_result < result:
                            max_result = result
                        dfs(_peak)
                        is_cutting = False
                        map_list[_peak[0]][_peak[1]][0] += cutting_value
                        map_list[_peak[0]][_peak[1]][1] = False
                        result -= 1


def dfs(_peak: list):
    global map_list
    global result
    global max_result
    if not 0 <= _peak[1] < n:
        return
    if not 0 <= _peak[0] < n:
        return
    for _dir_idx in range(4):
        return_temp = check_map(dir_idx=_dir_idx, _peak=_peak)
        if return_temp is not None:
            dfs(_peak)
            map_list[_peak[0]][_peak[1]][1] = False
            result -= 1

        nx, ny = dx[_dir_idx], dy[_dir_idx]
        _peak[0] = _peak[0] + ny * -1
        _peak[1] = _peak[1] + nx * -1


def breaking_brick(point: list):
    value = double_list_get_list(map_list, point)
    removed_list = []
    for dir_idx in range(len(dx)):
        temp_removed_list = []
        nx, ny = dx[dir_idx], dy[dir_idx]
        for value_index in range(1, value):
            new_point_h = point[0] + ny * value_index
            new_point_w = point[1] + nx * value_index
            new_point = [new_point_h, new_point_w]
            value = double_list_get_list(map_list, new_point)
            breaking_brick(new_point)
            print(value_index)
        removed_list.append(temp_removed_list)

    first_shout_result = first_shout()
    if first_shout_result == False:
        return
    elif first_shout_result == True:
        return True


test_case_num = int(input())


def find_top_level(w_pram):
    global map_list
    for _h_index in range(h):
        if map_list[_h_index][w_pram] != 0:
            return _h_index
    return -1


def first_shout():
    global n
    n -= 1
    if n == 0:
        return False
    for _w_index in range(w):
        h_index = find_top_level(_w_index)
        if h_index != -1:
            breaking_brick([h_index, _w_index])
    return True  # 벽돌을 다 깬 경우


for test_case_index in range(test_case_num):
    n, w, h = map(int, input().split())
    # 입력의 첫 번째 줄은 배열의 행 수입니다.
    map_list = []
    result = 0
    for i in range(h):
        temp_list = list(map(int, input().split()))
        for temp in temp_list:
            if temp != 0:
                result += 1
        map_list.append(temp_list)
    min_result = result
    first_shout()

    print("#%d %d" % (test_case_index + 1, min_result))

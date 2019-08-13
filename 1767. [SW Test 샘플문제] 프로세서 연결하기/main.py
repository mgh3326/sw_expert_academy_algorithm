import copy


def left_check(point, _map_list):
    h, w = point
    for _width in range(w):
        if _map_list[h][_width] != 0:
            for __width in range(_width):
                _map_list[h][__width] = 0

            _map_list[h][w] = 3
            return
        else:
            _map_list[h][_width] = 1
    _map_list[h][w] = 2
    global result
    result += 1
    global line
    line += w


def right_check(point, _map_list):
    h, w = point
    for _width in range(n - w - 1):
        if _map_list[h][n - _width - 1] != 0:
            for __width in range(n - _width - 1):
                _map_list[h][n - __width - 1] = 0
            _map_list[h][w] = 3
            return
        else:
            _map_list[h][n - _width - 1] = 1
    _map_list[h][w] = 2
    global result
    result += 1
    global line
    line += n - w - 1


def upper_check(point, _map_list):
    h, w = point
    for _height in range(h):
        if _map_list[_height][w] != 0:
            for __height in range(_height):
                _map_list[__height][w] = 0

            _map_list[h][w] = 3
            return
        else:
            _map_list[_height][w] = 1
    _map_list[h][w] = 2
    global result
    result += 1
    global line
    line += h


def down_check(point, _map_list):
    h, w = point

    for _height in range(n - h - 1):
        if _map_list[n - _height - 1][w] != 0:
            for __height in range(n - _height - 1):
                _map_list[__height][w] = 0

            _map_list[h][w] = 3
            return
        else:
            _map_list[n - _height - 1][w] = 1
    _map_list[h][w] = 2
    global result
    result += 1
    global line
    line += n - h - 1


def dfs(_map_list=None, _saved_list=[]):
    global result
    global max_result
    global line
    global min_line
    if len(_saved_list) == 0:
        if max_result < result:
            max_result = result
            min_line = line
        elif max_result == result:
            if min_line > line:
                min_line = line
        return
    saved_list_copy = copy.deepcopy(_saved_list)
    saved_list_copy_pop = saved_list_copy.pop(0)
    map_list_copy = copy.deepcopy(_map_list)
    _result_copy = result
    line_copy = line
    left_check(saved_list_copy_pop[0], _map_list)
    dfs(_map_list, saved_list_copy)
    _map_list = copy.deepcopy(map_list_copy)
    result = _result_copy
    line = line_copy
    right_check(saved_list_copy_pop[0], _map_list)
    dfs(_map_list, saved_list_copy)
    _map_list = copy.deepcopy(map_list_copy)
    result = _result_copy
    line = line_copy
    upper_check(saved_list_copy_pop[0], _map_list)
    dfs(_map_list, saved_list_copy)
    _map_list = copy.deepcopy(map_list_copy)
    result = _result_copy
    line = line_copy
    down_check(saved_list_copy_pop[0], _map_list)
    dfs(_map_list, saved_list_copy)
    _map_list = copy.deepcopy(map_list_copy)
    result = _result_copy
    line = line_copy
    dfs(_map_list, saved_list_copy)
    _map_list = copy.deepcopy(map_list_copy)
    result = _result_copy
    line = line_copy


test_case_num = int(input())

for test_case_index in range(test_case_num):
    n = int(input())
    result = 0

    max_result = 0
    # 입력의 첫 번째 줄은 배열의 행 수입니다.
    map_list = []
    # 입력을 받되 첫줄 혹은 끝줄의 경우 2(전선 연결 완료)로 표시하도록 하자
    saved_list = []
    for i in range(n):
        temp_list = list(map(int, input().split()))
        if i == 0 or i == n - 1:
            for idx, temp in enumerate(temp_list):
                if temp == 1:
                    temp_list[idx] = 2
                    result += 1

        else:
            for idx, temp in enumerate(temp_list):
                if idx == 0 or idx == n - 1:
                    if temp == 1:
                        temp_list[idx] = 2
                        result += 1
                        # saved_list.append([(i, idx), True])
                else:
                    if temp == 1:
                        saved_list.append([(i, idx), 0])

        map_list.append(temp_list)

    max_result = result
    line = 0
    min_line = n * n
    dfs(map_list, saved_list)

    print(min_line)

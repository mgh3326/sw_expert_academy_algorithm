def all_check(point, _map_list, direction):
    h, w = point
    global result
    global line
    remove_list = []
    if direction == 0:
        for _width in range(w):
            if _map_list[h][_width] != 0:
                for _remove in remove_list:
                    _map_list[h][_remove] = 0

                _map_list[h][w] = 3
                return
            else:
                remove_list.append(_width)
                _map_list[h][_width] = 1
        _map_list[h][w] = 2
        result += 1
        line += w
    elif direction == 1:
        for _width in range(n - w - 1):
            if _map_list[h][n - _width - 1] != 0:
                for _remove in remove_list:
                    _map_list[h][_remove] = 0
                _map_list[h][w] = 3
                return
            else:
                remove_list.append(n - _width - 1)
                _map_list[h][n - _width - 1] = 1
        _map_list[h][w] = 2
        result += 1
        line += n - w - 1
    elif direction == 2:
        for _height in range(h):
            if _map_list[_height][w] != 0:
                for _remove in remove_list:
                    _map_list[_remove][w] = 0

                _map_list[h][w] = 3
                return
            else:
                remove_list.append(_height)
                _map_list[_height][w] = 1
        _map_list[h][w] = 2
        result += 1
        line += h
    elif direction == 3:
        for _height in range(n - h - 1):
            if _map_list[n - _height - 1][w] != 0:
                for _remove in remove_list:
                    _map_list[_remove][w] = 0

                _map_list[h][w] = 3
                return
            else:
                remove_list.append(n - _height - 1)
                _map_list[n - _height - 1][w] = 1
        _map_list[h][w] = 2
        result += 1
        line += n - h - 1
    return True


def all_roll_back(point, _map_list, direction):
    h, w = point
    if direction == 0:
        for _width in range(w):
            _map_list[h][_width] = 0
    elif direction == 1:
        for _width in range(n - w - 1):
            _map_list[h][n - _width - 1] = 0
    elif direction == 2:
        for _height in range(h):
            _map_list[_height][w] = 0
    elif direction == 3:
        for _height in range(n - h - 1):
            _map_list[n - _height - 1][w] = 0


def dfs(_map_list=None, _saved_list=[]):
    global result
    global max_result
    global line
    global min_line
    saved_list_len = len(_saved_list)
    if saved_list_len + result < max_result:
        return
    if saved_list_len == 0:
        if max_result < result:
            max_result = result
            min_line = line
        elif max_result == result:
            if min_line > line:
                min_line = line
        return
    saved_list_copy = _saved_list.copy()
    saved_list_copy_pop = saved_list_copy.pop(0)
    _result_copy = result
    line_copy = line
    for _direction in range(4):
        reuslt_temp = all_check(saved_list_copy_pop[0], _map_list, _direction)
        dfs(_map_list, saved_list_copy)
        if reuslt_temp == True:
            all_roll_back(saved_list_copy_pop[0], _map_list, _direction)

        result = _result_copy
        line = line_copy
    dfs(_map_list, saved_list_copy)


test_case_num = int(input())

for test_case_index in range(test_case_num):
    n = int(input())
    result = 0

    max_result = 0
    # 입력의 첫 번째 줄은 배열의 행 수입니다.
    my_list = []
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

        my_list.append(temp_list)

    max_result = result
    line = 0
    min_line = n * n
    dfs(my_list, saved_list)

    print("#" + str(test_case_index + 1), min_line)

dx = [1, 0, -1, 0]  # Right, down, left, up
dy = [0, 1, 0, -1]
max_result = 1
is_cutting = False


def check_map(dir_idx: int, _peak: list):
    global map_list
    global result
    global max_result
    nx, ny = dx[dir_idx], dy[dir_idx]
    peak_value = map_list[_peak[0]][_peak[1]][0]
    _peak[0] = _peak[0] + ny
    _peak[1] = _peak[1] + nx
    if 0 <= _peak[1] < n and 0 <= _peak[0] < n and peak_value > map_list[_peak[0]][_peak[1]][0]:

        if map_list[_peak[0]][_peak[1]][1] == False:
            map_list[_peak[0]][_peak[1]][1] = True
            result += 1
            if max_result < result:
                max_result = result
            return True


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


test_case_num = int(input())
for test_case_index in range(test_case_num):
    n, k = map(int, input().split())
    # 입력의 첫 번째 줄은 배열의 행 수입니다.
    map_list = []
    max_value = 0
    peak_list = []
    for i in range(n):
        temp_list = list(map(int, input().split()))
        temp_max_value = max(temp_list)
        if temp_max_value > max_value:
            max_value = temp_max_value
        map_list.append(temp_list)

    for i in range(n):
        for j in range(n):
            if map_list[i][j] == max_value:
                peak_list.append([i, j])
            map_list[i][j] = [map_list[i][j], False]
    for peak in peak_list:
        map_list[peak[0]][peak[1]][1] = True
        result = 1
        dfs(peak)
        map_list[peak[0]][peak[1]][1] = False

    print(max_result)

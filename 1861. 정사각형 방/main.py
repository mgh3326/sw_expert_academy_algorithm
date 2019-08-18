dx = [1, 0, -1, 0]  # Right, down, left, up
dy = [0, 1, 0, -1]


def dfs(height: int, width: int):
    global max_value
    global current_value
    global result_value
    if not 0 <= height < n:
        return
    if not 0 <= width < n:
        return
    for nx, ny in zip(dx, dy):
        next_h = height + ny
        next_w = width + nx
        if not 0 <= next_h < n:
            continue
        if not 0 <= next_w < n:
            continue
        _current_value = my_list[height][width]
        next_value = my_list[next_h][next_w]
        if check_list[next_h][next_w] is False and next_value - _current_value == 1:
            check_list[next_h][next_w] = True
            current_value += 1
            if max_value < current_value:
                result_value = start_value
                max_value = current_value
            elif max_value == current_value:
                if result_value > start_value:
                    result_value = start_value

            dfs(next_h, next_w)
            current_value -= 1
            check_list[next_h][next_w] = False


test_case_num = int(input())
for test_case_index in range(test_case_num):
    n = int(input())
    result_value = []
    max_value = 0
    current_value = 0
    my_list = []
    check_list = []
    for i in range(n):
        check_list.append([False] * n)
        my_list.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            check_list[i][j] = True
            start_value = my_list[i][j]
            dfs(i, j)
            check_list[i][j] = False

    print("#" + str(test_case_index + 1), result_value, max_value + 1)

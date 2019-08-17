dx = [1, 0, -1, 0, 1, 1, -1, -1]  # Right, down, left, up, 1시, 5시, 7시, 11시
dy = [0, 1, 0, -1, 1, -1, -1, 1]

test_case_num = int(input())

for test_case_index in range(test_case_num):
    n, m = map(int, input().split())
    result0 = 0
    result1 = 0
    my_list = []
    go_board = []
    for i in range(n):
        if i == (n // 2) - 1:
            temp_list = [0] * ((n // 2) - 1)
            temp_list.extend([2, 1])
            temp_list.extend([0] * ((n // 2) - 1))
            go_board.append(temp_list)
        elif i == (n // 2):
            temp_list = [0] * ((n // 2) - 1)
            temp_list.extend([1, 2])
            temp_list.extend([0] * ((n // 2) - 1))
            go_board.append(temp_list)
        else:
            go_board.append([0] * n)
    for i in range(m):
        x, y, stone_kind = map(int, input().split())
        w = x - 1
        h = y - 1
        go_board[h][w] = stone_kind
        for nx, ny in zip(dx, dy):
            temp_w = w + nx
            temp_h = h + ny
            try:
                if (go_board[h][w] == 1 and go_board[temp_h][temp_w] == 2) or (
                        go_board[h][w] == 2 and go_board[temp_h][temp_w] == 1):
                    _temp_w = temp_w + nx
                    _temp_h = temp_h + ny
                    if (go_board[_temp_h][_temp_w] == 1 and go_board[temp_h][temp_w] == 2) or (
                            go_board[_temp_h][_temp_w] == 2 and go_board[temp_h][temp_w] == 1):
                        go_board[temp_h][temp_w] = stone_kind
            except IndexError:
                continue

    print("#" + str(test_case_index + 1), result0, result1)

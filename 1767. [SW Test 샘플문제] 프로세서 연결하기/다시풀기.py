import sys

sys.stdin = open("./data/sample_input.txt")

dh = [-1, 1, 0, 0]  # 상 하 좌 우
dw = [0, 0, -1, 1]  # 상 하 좌 우


def dfs(depth):
    global current_line_num
    global max_count
    global result
    if depth == len(core_dict_keys):
        core_len = len(core_dict) - list(core_dict.values()).count(4)
        if core_len > max_count:
            max_count = core_len
            result = current_line_num
        elif core_len == max_count:
            if result > current_line_num:
                result = current_line_num
        return

    while True:
        current_core_depth = core_dict[core_dict_keys[depth]]
        if current_core_depth == 5:
            core_dict[core_dict_keys[depth]] = 0
            break
        elif current_core_depth == 4:
            pass
        else:
            current_h, current_w = core_dict_keys[depth]
            nh = dh[current_core_depth]
            nw = dw[current_core_depth]
            temp_list = []
            is_ok = True
            while True:
                current_h += nh
                current_w += nw
                if current_h < 0 or current_w < 0 or current_h >= n or current_w >= n:
                    break
                if board_list[current_h][current_w] != 0:
                    is_ok = False
                    break
                temp_list.append((current_h, current_w))
            if is_ok:
                for h, w in temp_list:
                    board_list[h][w] = 2
                    current_line_num += 1
            else:
                core_dict[core_dict_keys[depth]] += 1
                continue

        dfs(depth + 1)
        if current_core_depth < 4:
            current_h, current_w = core_dict_keys[depth]
            while True:
                current_h += nh
                current_w += nw
                if current_h < 0 or current_w < 0 or current_h >= n or current_w >= n:
                    break
                board_list[current_h][current_w] = 0
                current_line_num -= 1
        core_dict[core_dict_keys[depth]] += 1


test_case_num = int(input())
for test_case_index in range(test_case_num):
    already_connect_num = 0
    max_count = 0
    result = 0
    current_line_num = 0
    n = int(input())
    board_list = []
    core_dict = {}
    for i in range(n):
        temp_list = list(map(int, input().split()))
        for j in range(n):
            if temp_list[j] == 1:
                if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                    already_connect_num += 1
                else:
                    core_dict[(i, j)] = 0
        board_list.append(temp_list)
    core_dict_keys = list(core_dict.keys())
    dfs(0)
    print("#%d %d" % (test_case_index + 1, result))

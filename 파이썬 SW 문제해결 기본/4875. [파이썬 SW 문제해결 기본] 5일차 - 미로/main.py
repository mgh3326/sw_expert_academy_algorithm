import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]


def dfs(current_h, current_w):
    global is_end
    global result
    for dir_idx in range(len(dh)):
        next_h = dh[dir_idx] + current_h
        next_w = dw[dir_idx] + current_w
        if next_h < 0 or next_w < 0 or next_h >= n or next_w >= n:
            continue
        if board_list[next_h][next_w] == 0 and visit_list[next_h][next_w] is False:
            visit_list[next_h][next_w] = True
            dfs(next_h, next_w)
            if is_end:
                return
            visit_list[next_h][next_w] = False
        elif board_list[next_h][next_w] == 3:
            is_end = True
            result = 1
            return


for test_case_index in range(test_case_num):
    is_end = False
    result = 0
    n = int(input())
    board_list = []
    visit_list = []
    start_h = 0
    start_w = 0
    for i in range(n):
        temp_value = input()
        temp_list = []
        for temp_index in range(len(temp_value)):
            temp = int(temp_value[temp_index])
            if temp == 2:
                start_h = i
                start_w = temp_index
            temp_list.append(temp)
        board_list.append(temp_list)
        visit_list.append([False] * n)
    visit_list[start_h][start_w] = True
    dfs(start_h, start_w)
    print("#%d %s" % (test_case_index + 1, result))

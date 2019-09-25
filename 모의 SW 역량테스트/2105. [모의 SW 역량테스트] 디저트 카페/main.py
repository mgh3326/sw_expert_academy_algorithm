import sys

sys.stdin = open("./data/sample_input.txt")

dh = [1, 1, -1, -1]  # 우아, 왼아, 우위, 왼위
dw = [1, -1, 1, -1]


def dfs(current_h, current_w, depth):
    global result
    if depth != 0 and current_h == start_h and current_w == start_w:
        if result < depth:
            result = depth
        return
    for dir_idx in range(len(dh)):
        next_h = current_h + dh[dir_idx]
        next_w = current_w + dw[dir_idx]
        if next_h >= n or next_w >= n or next_h < 0 or next_w < 0:
            continue
        next_point = (next_h, next_w)
        if next_point in visit_list:
            continue
        next_cake = my_list[next_h][next_w]
        if next_h == start_h and next_w == start_w:
            if depth == 1:
                continue
        else:
            if next_cake == my_list[start_h][start_w]:
                continue
            if next_cake in visit_cake_list:
                continue
        if dir_idx in dir_list:
            if dir_list[-1] != dir_idx:
                continue
        dir_list.append(dir_idx)
        visit_list.append(next_point)
        visit_cake_list.append(next_cake)
        dfs(next_h, next_w, depth + 1)
        visit_list.pop()
        visit_cake_list.pop()
        dir_list.pop()
    pass


test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = -1
    n = int(input())
    my_list = []
    for i in range(n):
        temp_list = list(map(int, input().split()))
        my_list.append(temp_list)
    for start_h in range(n):
        for start_w in range(n):
            visit_list = []
            visit_cake_list = []
            dir_list = []
            dfs(start_h, start_w, 0)

    print("#%d %d" % (test_case_index + 1, result))

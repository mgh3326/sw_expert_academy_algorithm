import sys

sys.stdin = open("./sample_input.txt")
# 오른쪽 아래
dh = [0, 1]
dw = [1, 0]
test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    m = int(input())
    board_list = []
    visit_list = []
    for i in range(m):
        temp_list = list(map(int, input().split()))
        board_list.append(temp_list)
        visit_list.append([-1] * m)
    start_h = 0
    start_w = 0
    visit_list[start_h][start_w] = board_list[start_h][start_w]
    queue = []
    queue.append((start_h, start_w))
    while True:
        if len(queue) == 0:
            break
        current_h, current_w = queue.pop(0)
        current_value = visit_list[current_h][current_w]
        for dir_idx in range(len(dh)):
            next_h = current_h + dh[dir_idx]
            next_w = current_w + dw[dir_idx]
            if next_h >= m or next_w >= m:
                continue
            visit_value = visit_list[next_h][next_w]
            next_value = board_list[next_h][next_w]
            if visit_value == -1 or visit_value > current_value + next_value:
                visit_list[next_h][next_w] = current_value + next_value
                if visit_value != -1:
                    # 기존에 들어있던 append 하지 않기
                    if (next_h, next_w) not in queue:
                        queue.append((next_h, next_w))
                else:
                    queue.append((next_h, next_w))
    result = visit_list[m - 1][m - 1]
    print("#%d %d" % (test_case_index + 1, result))

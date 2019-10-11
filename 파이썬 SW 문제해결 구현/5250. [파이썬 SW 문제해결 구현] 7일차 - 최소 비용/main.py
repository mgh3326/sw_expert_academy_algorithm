import sys

sys.stdin = open("./input.txt")

dh = [0, 1, 0, -1]  # 우 하 좌 상
dw = [1, 0, -1, 0]
test_case_num = int(input())
for test_case_index in range(test_case_num):
    n = int(input())
    board_list = []
    visit_list = []
    for i in range(n):
        temp_list = list(map(int, input().split()))
        board_list.append(temp_list)
        visit_list.append([-1] * n)
    start_h = 0
    start_w = 0
    queue = []
    visit_list[0][0] = 0
    queue.append([start_h, start_w])
    while True:
        if len(queue) == 0:
            break
        current_h, current_w = queue.pop(0)
        current_value = visit_list[current_h][current_w]
        for dir_idx in range(len(dh)):
            next_h = current_h + dh[dir_idx]
            next_w = current_w + dw[dir_idx]
            if next_h >= n or next_w >= n or next_h < 0 or next_w < 0:
                continue
            temp_next_value = 0
            if board_list[next_h][next_w] > board_list[current_h][current_w]:
                temp_next_value += (board_list[next_h][next_w] - board_list[current_h][current_w])
            temp_next_value += (current_value + 1)
            if visit_list[next_h][next_w] == -1 or visit_list[next_h][next_w] > temp_next_value:
                visit_list[next_h][next_w] = temp_next_value
                queue.append([next_h, next_w])  # 기존의 큐에 값이 있는지 확인하는게 시간이 엄청 오래 걸리는것 같다

    result = visit_list[-1][-1]
    print("#%d %d" % (test_case_index + 1, result))

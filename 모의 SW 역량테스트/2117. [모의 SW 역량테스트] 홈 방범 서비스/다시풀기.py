import sys

sys.stdin = open("./data/sample_input (12).txt")

dir_list = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]
T = int(input())
for test_case_idx in range(T):
    result = 0
    N, M = map(int, input().split())
    board_list = [list(map(int, input().split())) for i in range(N)]
    home_list = []
    for h in range(N):
        for w in range(N):
            if board_list[h][w] == 1:
                home_list.append((h, w))
    max_cost = len(home_list) * M
    service_list = []
    total_service_set = set()
    total_service_set.add((0, 0))
    size = 1
    while True:
        service_list.append(list(total_service_set))
        size += 1
        if size * size + (size - 1) * (size - 1) > max_cost:
            break
        for h, w in list(total_service_set):
            for dh, dw in dir_list:
                nh, nw = h + dh, w + dw
                if (nh, nw) in total_service_set:
                    continue
                total_service_set.add((nh, nw))
    is_end = False

    for h in range(N):
        if is_end:
            break
        for w in range(N):
            if is_end:
                break
            is_find = False
            for i in range(len(service_list)):
                if is_find:
                    break
                if is_end:
                    break
                current_service_size = len(service_list) - i
                temp_value = len(service_list[current_service_size - 1])
                count = 0
                for dh, dw in service_list[current_service_size - 1]:
                    nh, nw = h + dh, w + dw
                    if nh < 0 or nw < 0 or nh >= N or nw >= N:
                        continue
                    if board_list[nh][nw] == 1:
                        temp_value -= M
                        count += 1
                if temp_value <= 0:
                    is_find = True
                    if result < count:
                        result = count
                        if result == len(home_list):
                            is_end = True
                            break
    print("#%d %d" % (test_case_idx + 1, result))

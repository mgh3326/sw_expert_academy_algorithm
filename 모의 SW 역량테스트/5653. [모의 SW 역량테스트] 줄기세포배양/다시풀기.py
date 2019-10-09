import sys

sys.stdin = open("./data/sample_input.txt")

import heapq

dh = [-1, 1, 0, 0]  # 상 하 좌 우
dw = [0, 0, -1, 1]  # 상 하 좌 우
test_case_num = int(input())
for test_case_index in range(test_case_num):
    n, m, k = map(int, input().split())
    board_dict = {}
    living_list = []
    active_dict = {}
    for h in range(n):
        temp_list = list(map(int, input().split()))
        for w in range(m):
            if temp_list[w] != 0:
                board_dict[h, w] = temp_list[w]
                heapq.heappush(living_list, [temp_list[w], temp_list[w] * -1, (h, w)])
    current_time = 0
    while True:
        if current_time == k:
            break
        culture_list = []
        while True:
            if len(living_list) == 0:
                break
            current_value, origin_value, (h, w) = heapq.heappop(living_list)
            if current_value > 0:
                heapq.heappush(living_list, [current_value, origin_value, (h, w)])
                break
            else:
                origin_value *= -1
                culture_list.append([(h, w), origin_value])
                if origin_value > 1:
                    if origin_value - 1 not in active_dict:
                        active_dict[origin_value - 1] = 0
                    active_dict[origin_value - 1] += 1

        for living_idx in range(len(living_list)):
            living_list[living_idx][0] -= 1
        heapq.heapify(living_list)
        for culture in culture_list:
            (h, w), value = culture
            for dir_idx in range(len(dh)):
                nh = h + dh[dir_idx]
                nw = w + dw[dir_idx]
                if (nh, nw) not in board_dict:
                    board_dict[nh, nw] = value
                    heapq.heappush(living_list, [value, value * -1, (nh, nw)])
        if 0 in active_dict:
            active_dict.pop(0)
        temp_dict = {}
        for active_dict_keys in active_dict.keys():
            temp_dict[active_dict_keys - 1] = active_dict[active_dict_keys]
        active_dict = temp_dict
        current_time += 1
    result = len(living_list) + sum(active_dict.values())

    print("#%d %d" % (test_case_index + 1, result))

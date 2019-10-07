import sys

sys.stdin = open("./input.txt")

import heapq

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    n = int(input())
    board_list = []
    time_list = []
    time_set = set()
    save_list = []
    current_count = 0
    for i in range(n):
        start_time, end_time = (map(int, input().split()))
        heapq.heappush(time_list, [end_time - start_time, start_time, end_time])
    while True:
        if len(time_list) == 0:
            break
        _, start_time, end_time = heapq.heappop(time_list)
        temp_time_set = set()
        is_add = True
        for time in range(start_time, end_time):
            if time not in time_set:
                temp_time_set.add(time)
            else:
                is_add = False
                break
        if is_add:
            result += 1
            time_set = time_set.union(temp_time_set)

    print("#%d %d" % (test_case_index + 1, result))

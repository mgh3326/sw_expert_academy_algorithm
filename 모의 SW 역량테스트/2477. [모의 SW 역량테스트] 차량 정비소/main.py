import sys

sys.stdin = open("./data/input.txt")

import heapq

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = -1
    n, m, k, a, b = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    blank_a_list = []
    t_list = list(map(int, input().split()))
    current_a_list = []
    current_b_list = []
    ready_list = []
    current_index = 0
    first_time = t_list[current_index]
    ready_list.append(current_index + 1)
    while True:
        if current_index == len(t_list):
            break
        if first_time != t_list[current_index + 1]:
            break
        current_index += 1
        ready_list.append(current_index + 1)
    heapq.heapify(a_list)
    while True:
        if len(a_list) == 0:
            break
        if len(ready_list) == 0:
            break
        pop = ready_list.pop(0)
        heappop = heapq.heappop(a_list)
        heapq.heappush(current_a_list, [heappop, pop])
    print("#%d %d" % (test_case_index + 1, result))

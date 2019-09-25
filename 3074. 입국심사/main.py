import sys

sys.stdin = open("./data/input.txt")

import heapq

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    n, m = map(int, input().split())
    blank_list = []
    my_list = []
    for i in range(n):
        temp = int(input())
        heapq.heappush(blank_list, temp)
    current_index = 0
    while True:
        while True:
            if len(blank_list) == 0:
                break
            if current_index == m:
                break
            blank_min = heapq.heappop(blank_list)
            heapq.heappush(my_list, [blank_min, blank_min])
            current_index += 1
        if current_index == m:
            break
        temp_min = heapq.heappop(my_list)
        heapq.heappush(blank_list, temp_min[1])
        while True:
            if len(my_list) == 0:
                break
            heappop = heapq.heappop(my_list)
            if heappop[0] == temp_min[0]:
                heapq.heappush(blank_list, heappop[1])
            else:
                heapq.heappush(my_list, heappop)
                break
        result += temp_min[0]
        for i in range(len(my_list)):
            my_list[i][0] -= temp_min[0]
        heapq.heapify(my_list)
    # TODO 이익이 큰 쪽으로 가주어야하는 부분이 어렵다
    print("#%d %d" % (test_case_index + 1, result))

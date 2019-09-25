import sys

sys.stdin = open("./data/sample_input.txt")

import heapq

test_case_num = int(input())
for test_case_idx in range(test_case_num):
    n, k = map(int, input().split())
    num_str = input()
    save_list = []
    for j in range(n // 4):
        current_index = 0
        for i in range(4):
            temp_str = num_str[current_index:current_index + n // 4]
            hex_temp_str = int(temp_str, 16)
            minus_value = hex_temp_str * -1
            if minus_value not in save_list:
                heapq.heappush(save_list, minus_value)
            current_index += n // 4
        num_str = num_str[1:] + num_str[0]
    for i in range(k):
        heappop = heapq.heappop(save_list)
    current_count = heappop * -1
    print("#%d %d" % (test_case_idx + 1, current_count))

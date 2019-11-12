import sys

sys.stdin = open("./data/sample_input.txt")

import math


def dfs(depth):
    global min_value
    global max_value
    if depth == N - 1:
        min_value = min(min_value, save_list[-1])
        max_value = max(max_value, save_list[-1])
        return
    for idx in range(4):
        if operating_list[idx] == 0:
            continue
        current_num = save_list[-1]
        if idx == 0:
            current_num += number_list[depth + 1]
        elif idx == 1:
            current_num -= number_list[depth + 1]
        elif idx == 2:
            current_num *= number_list[depth + 1]
        elif idx == 3:
            if current_num / number_list[depth + 1] < 0:
                current_num = math.ceil(current_num / number_list[depth + 1])
            else:
                current_num //= number_list[depth + 1]
        save_list.append(current_num)
        operating_list[idx] -= 1
        dfs(depth + 1)
        operating_list[idx] += 1
        save_list.pop()


test_case_num = int(input())
for test_case_idx in range(test_case_num):
    N = int(input())
    operating_list = list(map(int, input().split()))
    number_list = list(map(int, input().split()))
    my_list = []
    min_value = 100000001
    max_value = -100000001
    for operating_idx, operating in enumerate(operating_list):
        my_list.extend([operating_idx] * operating)
    save_list = [number_list[0]]
    dfs(0)
    result = max_value - min_value
    print("#%d %d" % (test_case_idx + 1, result))

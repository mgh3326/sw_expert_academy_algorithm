import sys

sys.stdin = open("data/sample_input.txt")

import itertools

T = int(input())


def generate_my_list(depth, start_idx):
    if depth == M:
        my_list.append(temp_list.copy())

        return
    for idx in range(start_idx, N):
        if depth != 0 and idx - temp_list[-1] > 1:
            break
        temp_list.append(idx)
        generate_my_list(depth + 1, idx + 1)
        temp_list.pop()


for test_case_idx in range(T):
    result = 0
    N, M, C = map(int, input().split())
    board_list = [list(map(int, input().split())) for i in range(N)]
    temp_list = []
    my_list = []
    generate_my_list(0, 0)
    for i in range(N):
        for _j in range(N - i):
            j = N - _j - 1
            for k in range(len(my_list)):
                for m in range(len(my_list)):
                    first_idx_list = my_list[k]
                    second_idx_list = my_list[m]
                    if i == j:
                        if m >= k or len(set(first_idx_list).intersection(second_idx_list)) > 0:  # TODO 중복처리 잘해준걸까
                            continue
                    else:
                        first_list = []
                        first_value = 0
                        for first_idx in first_idx_list:
                            first_list.append(board_list[i][first_idx])
                        if sum(first_list) > C:
                            first_value = max(first_list) * max(first_list)
                            for size in (range(2, M)):
                                for combination in list(itertools.combinations(first_list, size)):
                                    if sum(combination) <= C:
                                        temp_first_value = 0
                                        for first in combination:
                                            temp_first_value += first * first
                                        first_value = max(first_value, temp_first_value)
                        else:
                            for first in first_list:
                                first_value += first * first
                        second_list = []
                        second_value = 0
                        for second_idx in second_idx_list:
                            second_list.append(board_list[j][second_idx])
                        if sum(second_list) > C:
                            second_value = max(second_list) * max(second_list)
                            for size in (range(2, M)):
                                for combination in list(itertools.combinations(second_list, size)):
                                    if sum(combination) <= C:
                                        temp_second_value = 0
                                        for second in combination:
                                            temp_second_value += second * second
                                        second_value = max(second_value, temp_second_value)

                        else:
                            for second in second_list:
                                second_value += second * second
                        if result < first_value + second_value:
                            result = first_value + second_value

    print("#%d %d" % (test_case_idx + 1, result))

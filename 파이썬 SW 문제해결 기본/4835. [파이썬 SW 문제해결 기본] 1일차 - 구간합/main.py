import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    n, m = map(int, input().split())
    number_list = list(map(int, input().split()))
    max_sum = 0
    min_sum = -1
    for i in range(n - m + 1):
        temp_value = 0
        for j in range(m):
            temp_value += number_list[i + j]
        if max_sum < temp_value:
            max_sum = temp_value
        if min_sum == -1 or min_sum > temp_value:
            min_sum = temp_value
    result = max_sum - min_sum
    print("#%d %d" % (test_case_index + 1, result))

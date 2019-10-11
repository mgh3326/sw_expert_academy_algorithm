import sys

sys.stdin = open("./input.txt")


def find_memo(input_n):
    if memo[input_n] != -1:
        return memo[input_n]
    memo[input_n] = find_memo(input_n - 3) + find_memo(input_n - 2) * 2 + find_memo(input_n - 1)
    return memo[input_n]


test_case_num = int(input())
for test_case_index in range(test_case_num):
    memo = [-1] * 31
    memo[0] = 1
    memo[1] = 1
    memo[2] = 3
    memo[3] = 6
    n = int(input())
    result = find_memo(n)
    print("#%d %d" % (test_case_index + 1, result))

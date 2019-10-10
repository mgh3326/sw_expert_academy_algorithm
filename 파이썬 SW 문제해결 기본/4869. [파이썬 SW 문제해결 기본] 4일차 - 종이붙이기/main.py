import sys

sys.stdin = open("./input.txt")


def find_memo(index):
    if memo[index] != -1:
        return memo[index]
    memo[index] = find_memo(index - 1) + find_memo(index - 2) * 2
    return memo[index]


test_case_num = int(input())
memo = [-1] * 301
memo[0] = 0
memo[1] = 1
memo[2] = 3
for test_case_index in range(test_case_num):
    n = int(input())
    result = find_memo(n//10)
    print("#%d %s" % (test_case_index + 1, result))

import sys

sys.stdin = open("./input.txt")


def find_memo(depth, current_sum):
    if memo[depth][current_sum] != -1:
        return memo[depth][current_sum]
    temp = 0
    if current_sum >= depth:
        temp = find_memo(depth - 1, current_sum - depth)
    memo[depth][current_sum] = temp + find_memo(depth - 1, current_sum)
    return memo[depth][current_sum]


test_case_num = int(input())
for test_case_index in range(test_case_num):
    n, k = map(int, input().split())
    # 1, 2, 3, 4, 5, ... , n
    sigma = (n * (n + 1)) // 2
    memo = []
    memo.append([0] * (sigma + 1))
    memo[0][0] = 1
    for i in range(n):
        memo.append([-1] * (sigma + 1))
    result = find_memo(n, k)
    print("#%d %d" % (test_case_index + 1, result))
